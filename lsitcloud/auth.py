from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from lsitcloud.models import Cache  # Replace `myapp` with your app name
import requests, json, random
import boto3
from botocore.exceptions import ClientError

# Initialize DynamoDB resource
session = boto3.Session(
    aws_access_key_id="AKIAZI2LE6EX5MT67CT5",
    aws_secret_access_key="ixYVq+GE4A6xxeWlcGxajyZ92mRe5M0LxNoq0fyq",
    #aws_session_token="your-session-token",  # Only required if using temporary credentials
    region_name="ap-south-1"  # Make sure the region is correct
)
dynamodb = session.resource('dynamodb', region_name='ap-south-1')  # Use your AWS region
table = dynamodb.Table('lsit-developments')  # Replace with your DynamoDB table name

def login(request):
    default_theme = Cache.objects.get(title="default_theme")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = True #request.POST.get('remember_me')  # "Remember Me" checkbox
        
        # Retrieve user from DynamoDB based on email (assuming the username is the email)
        user = None
        try:
            response = table.get_item(Key={'email': email})
            user = response.get('Item')  # Returns None if the item doesn't exist
        except Exception as e:
            user = None
        
        if user:
            # Check if the password matches the stored hashed password
            if check_password(password, user['password']):
                # Log the user in using Django's session
                request.session['fullname'] = user['fullname']
                request.session['contact'] = user['contact']
                request.session['email'] = user['email']
                
                # Handle session expiration for "Remember Me"
                if remember_me:
                    # Set the session to expire in 30 days if "Remember Me" is checked
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                else:
                    # Default session expiration (when the browser is closed)
                    request.session.set_expiry(0)  # Expire when the browser is closed
                
                # Send success response
                return render(request, "techmark/dashboard.html", {"default_theme": default_theme.theme, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
            else:
                return render(request, "techmark/signin.html", {"default_theme": default_theme.theme, "message": "Incorrect Password"})
        else:
            # User not found in the database
            return render(request, "techmark/signin.html", {"default_theme": default_theme.theme, "message": "User Not Found"})

def register(request):
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
                'fullname': user_fullname,
                'contact': user_contact,
                'password': user_password,  # Save the hashed password
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
    # Clear all session data
    request.session.flush()
    default_theme = Cache.objects.get(title="default_theme")
    return render(request, "techmark/signin.html", {"default_theme": default_theme.theme})