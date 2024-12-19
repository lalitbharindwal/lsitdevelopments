from django.shortcuts import render
from myadmin.models import Myadmin
from lsitcloud.models import lsitcloud
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import boto3, random, requests, json

session = boto3.Session(
    aws_access_key_id="AKIAZI2LE6EX5MT67CT5",
    aws_secret_access_key="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",
    region_name="ap-south-1"
)
dynamodb = session.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('lsit-developments')

# Create your views here.
def home(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        return render(request, "home.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})

def login(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = True
        
        # Retrieve user from DynamoDB based on email (assuming the username is the email)
        user = None
        try:
            response = table.get_item(Key={'email': email})
            user = response.get('Item')  # Returns None if the item doesn't exist
        except Exception as e:
            user = None
        
        if user:
            # Check if the password matches the stored hashed password
            if check_password(password, user['userinfo']['password']):
                # Log the user in using Django's session
                request.session['fullname'] = user['userinfo']['fullname']
                request.session['contact'] = user['userinfo']['contact']
                request.session['email'] = user['userinfo']['email']
                obj, created = lsitcloud.objects.get_or_create(key=user['userinfo']['email'])
                obj.value = json.dumps(user)
                obj.save()
                # Handle session expiration for "Remember Me"
                if remember_me:
                    # Set the session to expire in 30 days if "Remember Me" is checked
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                else:
                    # Default session expiration (when the browser is closed)
                    request.session.set_expiry(0)  # Expire when the browser is closed
                
                # Send success response
                return home(request)
            else:
                return render(request, "login.html", {"default_theme": default_theme.value, "message": "Incorrect Password"})
        else:
            # User not found in the database
            return render(request, "login.html", {"default_theme": default_theme.value, "message": "User Not Found"})

    else:
        if request.session.get('email'):
            return render(request, "home.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
        else:
            return render(request, "login.html", {"default_theme": default_theme.value})

def signup(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.method == 'POST':
        # Get input from form
        user_fullname = request.POST.get('fullname')
        user_email = request.POST.get('email')
        user_contact = request.POST.get('contact-number')
        user_password = request.POST.get('password')
        user_confirm_password = request.POST.get('confirm-password')
        
        # Check if passwords match
        if user_password != user_confirm_password:
            return JsonResponse({"success": False, "message": "Passwords do not match."})

        # Hash the password (recommended for storing passwords securely)
        hashed_password = make_password(user_password)
        
        # Save the user details in session to be used later in OTP verification
        request.session['user_fullname'] = user_fullname
        request.session['user_email'] = user_email
        request.session['user_contact'] = user_contact
        request.session['user_password'] = hashed_password  # Store hashed password in session

        # Generate OTP and store it in session
        otp = generate_otp()
        request.session['otp'] = otp
        request.session['otp_verified'] = False  # Set OTP verification status to False
        
        # Create payload for OTP email
        payload = {
            "fullname": user_fullname,
            "email": user_email,
            "code": otp  # Generated OTP code
        }

        # Send OTP and handle response
        response = send_otp(payload)  # Assuming send_otp is a function that sends the email
        if response.status_code == 200:
            return JsonResponse({"success": True, "message": "OTP sent for verification."})
        else:
            return JsonResponse({"success": False, "message": "Failed to send OTP. Please try again later."})
        
    else:
        return render(request, "signup.html", {"default_theme": default_theme.value})

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

def verifyOtp(request):
    if request.method == 'POST':
        # Get input from form
        user_otp = request.POST.get('otp')
        # Retrieve OTP from session
        stored_otp = request.session.get('otp')
        # Verify if the OTP matches and mark as verified
        if stored_otp and user_otp == stored_otp:
            request.session['otp_verified'] = True  # Mark as verified
            # Retrieve user details from session
            user_fullname = request.session.get('user_fullname')
            user_email = request.session.get('user_email')
            user_contact = request.session.get('user_contact')
            user_password = request.session.get('user_password')

            # Prepare the item to insert into DynamoDB
            item = {
                'email': user_email,  # Assuming email is the primary key
                'userinfo': {
                    'fullname': user_fullname,
                    'email': user_email,
                    'contact': user_contact,
                    'password': user_password,  # Save the hashed password
                },
                'lsdb': {'lsdbtables':{}}
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