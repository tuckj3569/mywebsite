from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def home(request):
	cars = Car.objects.all()
	return render(request, 'home.html',{'cars': cars})

	
def car_details(request, id):
	try:
		cars = Car.objects.all()
	except Car.DoesNotExist:
		raise Http404('car not found')
	return render(request, 'car_details.html', {'car':car})