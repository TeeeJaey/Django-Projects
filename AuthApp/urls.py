
from django.conf.urls import url,include
from django.urls import path
from AuthApp import views as AView

app_name = 'AuthApp'


urlpatterns = [    
    path('signUp/',AView.userSignUp, name='signUp'),
    path('signIn/',AView.userSignIn, name='signIn'),
    path('signOut/',AView.userSignOut, name='signOut'),

]