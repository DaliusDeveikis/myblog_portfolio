from django.urls import path

from . import views

app_name = 'signup'

urlpatterns = [
    path('', views.signupuser, name='signupuser'),
    path('current/', views.currentsignup, name='currentsignup'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('createuser/', views.createuser_blog, name='createuser'),
]
