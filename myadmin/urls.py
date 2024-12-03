from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),  # Example route
    path('signin', views.signin, name='signin'),  # Example route
    path('admin', views.admin, name='admin'),  # Example route
    path('themes', views.themes, name='themes'),  # Example route
    path('logout', views.logout, name='logout'),  # Example route
]