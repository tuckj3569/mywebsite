from django.contrib import admin

# Register your models here.
from .models import Car,Orders,Store,Customer
from django.contrib.admin import SimpleListFilter

def display_local_cars(modeladmin, request, queryset):
	for qs in queryset:
		print(qs.Car_ID)
		

class carModelFilter(SimpleListFilter):
	title = 'Car Model' # or use _('country') for translated title
	parameter_name = 'Car_Model'
	
	def lookups(self, request, model_admin):
		list_of_cars = []
		queryset = Car.objects.all()
		for car in queryset:
			list_of_cars.append(
				(str(car.Car_Model), car.Car_Model)
			)
		return sorted(list_of_cars, key=lambda tp: tp[1])
		
	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(Car_Model=self.value())

# class carYearFilter(SimpleListFilter):
	# title = 'Car Year' # or use _('country') for translated title
	# parameter_name = 'Car_SeriesYear'
	
	# def lookups(self, request, model_admin):
		# cars = Car.objects.all()
		# print(cars)
		# return [(c.Car_SeriesYear, c.Car_SeriesYear) for c in cars] + [(self.value())]

	# def queryset(self, request, queryset):
		# if self.value():
			# return queryset.filter(Car_SeriesYear=self.value())

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display=['Car_MakeName','Car_Model','Car_Series','Car_SeriesYear','Car_PriceNew']
	actions = [display_local_cars]
	list_filter = [carModelFilter]

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
	list_display=['Order_ID']
	
	
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display=['Store_Name']
	
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display=['Customer_ID']
	