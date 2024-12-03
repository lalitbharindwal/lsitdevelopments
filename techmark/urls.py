from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),  # Example route
    path('login', views.login, name='login'),  # Example route
    path('signup', views.signup, name='signup'),  # Example route
    path('verifyotp', views.verifyOtp, name='verifyOtp'),  # Example route
    path('logout', views.logout, name='logout'),  # Example route
]