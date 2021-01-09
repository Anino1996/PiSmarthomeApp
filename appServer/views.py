from django.shortcuts import render
from django.http import HttpResponse
from BoardSwitch import smartPin

lightPin=smartPin(4)
# Create your views here.
def SwitchView(request):
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
	return render(request,'api/home.html',ctx)
