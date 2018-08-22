from django.contrib import admin

# Register your models here.
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display=['Car_MakeName','Car_Model','Car_Series','Car_SeriesYear','Car_PriceNew']