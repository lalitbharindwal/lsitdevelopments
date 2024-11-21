from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from lsitcloud.models import Cache  # Replace `myapp` with your app name
import json

def signin(request):
    default_theme = Cache.objects.get(title="default_theme")
    return render(request, "lsitcloud/signin.html", {"default_theme": default_theme.theme})

def signup(request):
    default_theme = Cache.objects.get(title="default_theme")
    return render(request, "lsitcloud/signup.html", {"default_theme": default_theme.theme})

def dashboard(request):
    default_theme = Cache.objects.get(title="default_theme")
    return render(request, "lsitcloud/dashboard.html", {"default_theme": default_theme.theme})

def admin(request):
    default_theme = Cache.objects.get(title="default_theme")
    return render(request, "lsitcloud/admin.html", {"default_theme": default_theme.theme})

def themes(request):
    default_theme = Cache.objects.get(title="default_theme")
    return render(request, "lsitcloud/themes.html", {"default_theme": default_theme.theme})

def save_theme(request):
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

    return JsonResponse({"status": "error", "message": "Invalid request method."})
