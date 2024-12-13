from django.urls import path
from . import views

urlpatterns = [
    path('', views.techmarklogin, name='techmarklogin'),  # Example route
    path('index', views.index, name='index'),  # Example route
    path('addcampaign', views.addcampaign, name='addcampaign'),  # Example route
    path('techmarklogin', views.techmarklogin, name='techmarklogin'),  # Example route
    path('register', views.register, name='register'),  # Example route
    path('verifyotp', views.verifyotp, name='verifyotp'),
    path('logout', views.logout, name='logout'),
]