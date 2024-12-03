from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from lsitcloud.models import Cache  # Replace `myapp` with your app name
import json
default_theme = Cache.objects.get(title="default_theme")

def admin(request):
    if request.session.get('email') == "lsitdevelopments@gmail.com":
        return render(request, "myadmin/admin.html", {"default_theme": default_theme.theme, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
    else:
        return render(request, "myadmin/signin.html", {"default_theme": default_theme.theme})

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = True #request.POST.get('remember_me')  # "Remember Me" checkbox
        
        # Retrieve user from DynamoDB based on email (assuming the username is the email)
        user = None
        try:
            if email == "lsitdevelopments@gmail.com":
                user = "lsitdevelopments@gmail.com"
        except Exception as e:
            user = None
        
        if user:
            # Check if the password matches the stored hashed password
            if password == "Lalit@192":
                # Log the user in using Django's session
                request.session['fullname'] = "Lalit Sharma"
                request.session['contact'] = "08796775563"
                request.session['email'] = user
                
                # Handle session expiration for "Remember Me"
                if remember_me:
                    # Set the session to expire in 30 days if "Remember Me" is checked
                    request.session.set_expiry(30 * 24 * 60 * 60)  # 30 days in seconds
                else:
                    # Default session expiration (when the browser is closed)
                    request.session.set_expiry(0)  # Expire when the browser is closed
                
                # Send success response
                return render(request, "myadmin/admin.html", {"default_theme": default_theme.theme, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
            else:
                return render(request, "myadmin/signin.html", {"default_theme": default_theme.theme, "message": "Incorrect Password"})
        else:
            # User not found in the database
            return render(request, "myadmin/signin.html", {"default_theme": default_theme.theme, "message": "User Not Found"})

    else:
        if request.session.get('email') == "lsitdevelopments@gmail.com":
            return render(request, "myadmin/admin.html", {"default_theme": default_theme.theme, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
        else:
            return render(request, "myadmin/signin.html", {"default_theme": default_theme.theme})

def theme(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            theme_data = json.loads(request.body)
            # Use `get_or_create` to fetch or create a cache entry
            cache, created = Cache.objects.get_or_create(title='default_theme')
            # Update the theme field
            cache.theme = json.dumps(theme_data)  # Serialize the JSON data as a string
            cache.save()
            # Return appropriate response
            if created:
                return JsonResponse({"status": "created", "message": "New cache created."})
            else:
                return JsonResponse({"status": "updated", "message": "Cache updated successfully."})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON data."})

    else:
        if request.session.get('email') == "lsitdevelopments@gmail.com":
            return render(request, "myadmin/themes.html", {"default_theme": default_theme.theme, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
        else:
            return render(request, "myadmin/signin.html", {"default_theme": default_theme.theme})
    
def logout(request):
    # Clear all session data
    request.session.flush()