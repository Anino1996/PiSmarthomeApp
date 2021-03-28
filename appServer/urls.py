from django.urls import path
from .views import *
from django.contrib import admin

app_name='appserver'

urlpatterns=[
	path('', SwitchView, name='main'),
	path('mlogin', logView.as_view(), name='login'),
	path('logout', logoutView, name='logout'),
	]
