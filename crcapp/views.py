from django.shortcuts import render
from django.http import HttpResponse,Http404

from crcapp.models import Car

def home(request):
	cars = Car.objects.all()
	return render(request, 'home.html',{'cars': cars})

	
def car_details(request, id):
	try:
		car = Car.objects.get(Car_ID=id)
	except Car.DoesNotExist:
		raise Http404('Car not found')
	return render(request, 'car_details.html', {'car':car})