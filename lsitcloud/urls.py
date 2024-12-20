from django.urls import path
from . import views, lsdb

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('verifyotp', views.verifyOtp, name='verifyOtp'),
    path('logout', views.logout, name='logout'),
    path('lsdbtables', lsdb.lsdbtables, name='lsdbtables'),
    path('lsdbtabledetails', lsdb.lsdbtabledetails, name='lsdbtabledetails'),
    path('lsdbtableitems', lsdb.lsdbtableitems, name='lsdbtableitems'),
    path('lsdbcreatetable', lsdb.lsdbcreatetable, name='lsdbcreatetable'),
    path('lsdbdeletetable', lsdb.lsdbdeletetable, name='lsdbdeletetable'),
    path('lsdbdeleteattribute', lsdb.lsdbdeleteattribute, name='lsdbdeleteattribute'),
    path('lsdbputitems', lsdb.lsdbputitems, name='lsdbputitems'),
    path('lsdbapi', lsdb.lsdbapi, name='lsdbapi')
]