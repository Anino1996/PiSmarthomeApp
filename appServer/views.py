from django.shortcuts import render, redirect
from django.http import HttpResponse
from BoardSwitch import smartPin
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.mixins import LoginRequiredMixin
lightPin=smartPin(4)
# Create your views here.

class SwitchView(View):
	def get(self, request):

		if not request.user.is_authenticated:
			return redirect('login')

		command=request.GET.get('cmd')
		fdbck='Light on' if lightPin.is_active else 'Light off'
		if command:
			if command.lower()=='on':
				lightPin.switch_on()	
				fdbck='Light on' if lightPin.is_active else 'Error occurred'
			elif command.lower()=='off':
				lightPin.switch_off()		
				fdbck='Light off' if not lightPin.is_active else 'Error occurred'
			else:
				fdbck='Invalid request'
		ctx={'cmd':fdbck}
		return render(request,'appServer/home.html',ctx)

class loginView(View):

	def get(self, request):
		form=LoginForm()
		ctx={'form':form}
		return render(request, 'manual_login.html', ctx)

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

