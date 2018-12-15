from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from Devices.models import Device


def switch_device(request, id=None):
	"""This function is for switching the device"""
	device = get_object_or_404(Device, id=id)
	if request.method == 'POST':
		print(request.POST)
		try:
			state = request.POST['state']
		except:
			state = 'off'
		if state == 'on':
			device.state = True
		else:
			device.state = False
		device.save()
	context = {
	'state':device.state, 'instance':device,
	}
	return render(request, 'device.html', context)

def show_state(request, id=None):
	"""This function is to help view the current state of the device, it returns a json response"""
	device = get_object_or_404(Device, id=id)
	return JsonResponse({'state':device.state})

def home(request):
	#this is not really important for the demonstration of this project but let just make our website have a homepage
	return render(request, 'home.html',)