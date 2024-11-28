from django.urls import path
from . import views, auth

urlpatterns = [
    path('', views.signin, name='signin'),  # Example route
    path('signin', views.signin, name='signin'),  # Example route
    path('login', auth.login, name='login'),
    path('signup', views.signup, name='signup'),  # Example route
    path('register', auth.register, name='register'),  # Example route
    path('verifyotp', auth.verifyOtp, name='verifyotp'),  # Example route
    path('logout', auth.logout, name='logout'),  # Example route
    path('dashboard', views.dashboard, name='dashboard'),  # Example route
    path('admin', views.admin, name='admin'),  # Example route
    path('themes', views.themes, name='themes'),  # Example route
    path('save_theme', views.save_theme, name='save_theme'),
]