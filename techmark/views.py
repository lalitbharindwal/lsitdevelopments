from django.shortcuts import render
from myadmin.models import Myadmin
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, "index.html")

def techmarklogin(request):
    return render(request, "techmarklogin.html")

def techmarksignup(request):
    return render(request, "techmarksignup.html")