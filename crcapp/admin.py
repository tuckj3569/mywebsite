from django.contrib import admin

# Register your models here.
from .models import Car,Orders,Store,Customer

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display=['Car_MakeName','Car_Model','Car_Series','Car_SeriesYear','Car_PriceNew']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
	list_display=['Order_ID']
	
	
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display=['Store_Name']
	
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display=['Customer_ID']