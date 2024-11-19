from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),  # Example route
    path('admin', views.admin, name='admin'),  # Example route
    path('themes', views.themes, name='themes'),  # Example route
    path('save_theme', views.save_theme, name='save_theme'),
]