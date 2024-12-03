from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from myadmin.models import Myadmin  # Replace `myapp` with your app name
import json

# Create your views here.
def home(request):
    default_theme = Myadmin.objects.get(title="default_theme")
    if request.session.get('email') == "lsitdevelopments@gmail.com":
        return render(request, "home.html", {"default_theme": default_theme.theme, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
    else:
        return render(request, "home.html", {"default_theme": default_theme.theme})