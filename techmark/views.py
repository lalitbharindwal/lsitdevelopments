from django.shortcuts import render
from django.http import JsonResponse
from techmark.models import techmark
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import json, random, requests, boto3
# Initialize DynamoDB resource
session = boto3.Session(
    aws_access_key_id="AKIAZI2LE6EX5MT67CT5",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)
dynamodb = session.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('techmark-solutions')

def index(request):
    if request.session.get('email'):
        return render(request, "index.html")
    else:
        return render(request, "techmarklogin.html")

def techmarklogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = True
        user = None
        try:
            response = table.get_item(Key={'email': email})
            user = response.get('Item')  # Returns None if the item doesn't exist
        except Exception as e:
            user = None
        
        if user:
            if check_password(password, user['userinfo']['password']):
                request.session['fullname'] = user['userinfo']['fullname']
                request.session['email'] = user['userinfo']['email']
                obj, created = techmark.objects.get_or_create(key=user['userinfo']['email'])
                obj.value = json.dumps(user)
                obj.save()
                # Handle session expiration for "Remember Me"
                if remember_me:
                    # Set the session to expire in 30 days if "Remember Me" is checked
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                else:
                    # Default session expiration (when the browser is closed)
                    request.session.set_expiry(0)  # Expire when the browser is closed
                
                return index(request)
            else:
                return render(request, "techmarklogin.html", {"message": "Incorrect Password"})
        else:
            return render(request, "techmarklogin.html", {"message": "User Not Found"})

    else:
        if request.session.get('email'):
            return render(request, "index.html")
        else:
            return render(request, "techmarklogin.html")

def register(request):
    if request.method == 'POST':
        # Get input from form
        data = json.loads(request.body)
        # Hash the password (recommended for storing passwords securely)
        hashed_password = make_password(data["password"])
        
        # Save the user details in session to be used later in OTP verification
        request.session['user_fullname'] = data["fullname"]
        request.session['user_email'] = data["email"]
        request.session['user_contact'] = data["contact-number"]
        request.session['user_password'] = hashed_password  # Store hashed password in session
        request.session['user_createdon'] = data["createdon"]

        # Generate OTP and store it in session
        otp = generate_otp()
        request.session['otp'] = otp
        request.session['otp_verified'] = False  # Set OTP verification status to False
        
        # Create payload for OTP email
        payload = {
            "fullname": data["fullname"],
            "email": data["email"],
            "code": otp
        }

        # Send OTP and handle response
        response = send_otp(payload)  # Assuming send_otp is a function that sends the email
        if response.status_code == 200:
            return JsonResponse({"success": True, "message": "OTP sent for verification."})
        else:
            return JsonResponse({"success": False, "message": "Failed to send OTP. Please try again later."})
        
    else:
        return render(request, "techmarksignup.html")

def send_otp(payload):
    content = (
        f"Dear {payload['fullname']},\n\n"
        f"Your OTP is {payload['code']}\n"
        "Do not share it with anyone by any means.\n"
        "Code is only valid for 5 minutes\n\n"
        "Regards,\nTechMark Team"
    )
    
    data = {
        "name": payload["fullname"],
        "to": payload["email"],
        "subject": "Verify your Email for TechMark",
        "content": content
    }
    
    try:
        response = requests.post(
            'https://5v7v92mmsd.execute-api.us-east-1.amazonaws.com/techmark-notifications',
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        # Return the response to the caller for further status check
        return response
    
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        # Return None or a custom error response to signify failure
        return None

def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def verifyotp(request):
    if request.method == 'POST':
        # Get input from form
        user_otp = json.loads(request.body)
        # Retrieve OTP from session
        stored_otp = request.session.get('otp')
        # Verify if the OTP matches and mark as verified
        if stored_otp and user_otp["otp"] == stored_otp:
            request.session['otp_verified'] = True  # Mark as verified
            # Retrieve user details from session
            user_fullname = request.session.get('user_fullname')
            user_email = request.session.get('user_email')
            user_contact = request.session.get('user_contact')
            user_createdon = request.session.get('user_createdon')
            user_password = request.session.get('user_password')

            # Prepare the item to insert into DynamoDB
            item = {
                'email': user_email,  # Assuming email is the primary key
                'userinfo': {
                    'fullname': user_fullname,
                    'email': user_email,
                    'contact': user_contact,
                    'createdon': user_createdon,
                    'password': user_password,  # Save the hashed password
                },
                'email-campaigns': {'email-credentials':{}}
            }
            # Insert the data into DynamoDB
            response = table.put_item(Item=item)
            # Check if the response was successful
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return JsonResponse({"success": True, "message": "OTP verified successfully"})
            else:
                return JsonResponse({"success": False, "message": "Try Again Later"})
        else:
            return JsonResponse({"success": False, "message": "Incorrect OTP"})

    return JsonResponse({"success": False, "message": "Invalid request."})

def logout(request):
    request.session.flush()
    return JsonResponse({"status": "success", "message": "Logout Successfully"})