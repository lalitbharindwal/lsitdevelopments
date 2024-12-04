from django.urls import path
from . import views

urlpatterns = [
    path('', views.techmarklogin, name='techmarklogin'),  # Example route
    path('index', views.index, name='index'),  # Example route
    path('techmarklogin', views.techmarklogin, name='techmarklogin'),  # Example route
    path('techmarksignup', views.techmarksignup, name='techmarksignup')  # Example route
]