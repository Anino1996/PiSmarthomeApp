from django.urls import path
from . import views

app_name='appserver'

urlpatterns=[
	path('', views.SwitchView, name='switch')
	]