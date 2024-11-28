from django.urls import path
from . import views, techmark

urlpatterns = [
    path('', views.signin, name='signin'),  # Example route
    path('admin', views.admin, name='admin'),  # Example route
    path('signin', views.signin, name='signin'),  # Example route
    path('logout', views.logout, name='logout'),  # Example route
    path('theme', views.theme, name='theme'),  # Example route
    path('login', techmark.login, name='login'),
    path('signup', techmark.signup, name='signup'),  # Example route
    path('verifyotp', techmark.verifyOtp, name='verifyotp'),  # Example route
    path('dashboard', techmark.dashboard, name='dashboard')  # Example route
]