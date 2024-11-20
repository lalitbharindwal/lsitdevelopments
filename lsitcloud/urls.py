from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),  # Example route
    path('signin', views.signin, name='signin'),  # Example route
    path('signup', views.signup, name='signup'),  # Example route
    path('admin', views.admin, name='admin'),  # Example route
    path('themes', views.themes, name='themes'),  # Example route
    path('save_theme', views.save_theme, name='save_theme'),
]