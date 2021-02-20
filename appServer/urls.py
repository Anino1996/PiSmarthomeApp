from django.urls import path
from . import views

app_name='appserver'

urlpatterns=[
	path('', views.SwitchView.as_view(), name='main'),
	path('mlogin', views.loginView.as_view(), name='login'),
	]
