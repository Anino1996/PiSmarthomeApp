from django.shortcuts import render, redirect
from django.http import HttpResponse
from BoardSwitch import smartPin
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.mixins import LoginRequiredMixin
lightPin=smartPin(4)
# Create your views here.

# Decorator to check if user is logged in
def loginwrap(func):
	def  wrapper_func(request):
		if not request.user.is_authenticated:
			return redirect('login')

		return func(request)

	return wrapper_func


class SwitchView(View): #Main page to switch device on and off

# Wrap page  in authentication decorator

	@loginwrap
	def get(self, request):

# Get command passed by pressing button
		command=request.GET.get('cmd')

# Check device  status 
		fdbck='Light on' if lightPin.is_active else 'Light off'

# Turn device on or off based on command
		if command:
			if command.lower()=='on':
				lightPin.switch_on()	
				fdbck=command.lower() if lightPin.is_active else 'Error occurred'
			elif command.lower()=='off':
				lightPin.switch_off()		
				fdbck=command.lower() if not lightPin.is_active else 'Error occurred'
			else:
				fdbck='Invalid request'
		ctx={'cmd':fdbck}
		return render(request,'appServer/home.html',ctx)


# Handles manual login using authenticate

class logView(View):


	def get(self, request):

# Create empty form and pass as context 
		form=LoginForm()
		ctx={'form':form}
		return render(request, 'appServer/manual_login.html', ctx)


	def post(self, request):
		recv=request.POST
		username=recv.get('username'), 
		password=recv.get('password')
		form=loginForm(username=username, password=password)

		if form.is_valid():
			user=authenticate(request, username=username, password=password)

			if user:
				login(request, user)

				return redirect('main')

		ctx={'form':form}
		return render(request, 'appServer/manual_login.html', ctx)

