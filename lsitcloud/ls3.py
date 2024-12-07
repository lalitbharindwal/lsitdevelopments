from django.shortcuts import render
from myadmin.models import Myadmin

def ls3containers(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        return render(request, "ls3containers.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})

def ls3api(request):
    default_theme = Myadmin.objects.get(key="default_theme")
    if request.session.get('email'):
        return render(request, "ls3api.html", {"default_theme": default_theme.value, "email": request.session.get('email'), "fullname": request.session.get('fullname')})
    else:
        return render(request, "login.html", {"default_theme": default_theme.value})