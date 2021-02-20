from django.shortcuts import render
from django.http import HttpResponse
from BoardSwitch import smartPin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
lightPin=smartPin(4)
# Create your views here.
class SwitchView(LoginRequiredMixin, View):
	def get(self, request):
		command=request.GET.get('cmd')
		fdbck='Light on' if lightPin.is_active else 'Light off'
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
