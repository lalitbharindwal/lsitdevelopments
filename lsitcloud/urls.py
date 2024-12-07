from django.urls import path
from . import views, lsdb, ls3

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('verifyotp', views.verifyOtp, name='verifyOtp'),
    path('logout', views.logout, name='logout'),
    path('lsdbtables', lsdb.lsdbtables, name='lsdbtables'),
    path('createtable', lsdb.createtable, name='createtable'),
    path('lsdbapi', lsdb.lsdbapi, name='lsdbapi'),
    path('ls3containers', ls3.ls3containers, name='ls3containers'),
    path('ls3api', ls3.ls3api, name='ls3api'),
]