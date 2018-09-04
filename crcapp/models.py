from django.db import models

# Create your models here.
class Car(models.Model):
	FUEL_CHOICE = ['Petrol', 'Diesel', 'LPG']
	Car_ID = models.CharField(primary_key=True,max_length=10, blank=True)
	Car_MakeName = models.CharField(max_length=30, blank=True)
	Car_Model = models.CharField(max_length=30, blank=True)
	Car_Series = models.CharField(max_length=30, blank=True)
	Car_SeriesYear = models.CharField(max_length=30, blank=True)
	Car_PriceNew = models.CharField(max_length=30, blank=True)
	Car_EngineSize = models.CharField(max_length=30, blank=True)
	Car_FuelSystem = models.CharField(max_length=10, blank=True)
	Car_TankCapacity = models.CharField(max_length=10, blank=True)
	Car_Power = models.CharField(max_length=10, blank=True)
	Car_SeatingCapacity = models.CharField(max_length=10, blank=True)
	Car_StandardTransmission = models.CharField(max_length=10, blank=True)
	Car_BodyType = models.CharField(max_length=10, blank=True)
	Car_Drive = models.CharField(max_length=10, blank=True)
	Car_Wheelbase = models.CharField(max_length=10, blank=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.Car_Model

class Store(models.Model):
	Store_ID = models.CharField(primary_key=True,max_length=10, blank=True)
	Store_Name = models.CharField(max_length=10, blank=True)
	Store_Address = models.CharField(max_length=10, blank=True)
	Store_Phone = models.CharField(max_length=10, blank=True)
	Store_City = models.CharField(max_length=10, blank=True)
	Store_State = models.CharField(max_length=10, blank=True)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.Store_Name

class Customer(models.Model):	
	Customer_ID = models.CharField(primary_key=True,max_length=10, blank=True)
	Customer_Name = models.CharField(max_length=10, blank=True)
	Customer_Phone = models.CharField(max_length=10, blank=True)
	Customer_Addresss = models.CharField(max_length=10, blank=True)
	Customer_Brithday = models.CharField(max_length=10, blank=True)
	Customer_Occupation = models.CharField(max_length=10, blank=True)
	Customer_Gender = models.CharField(max_length=10, blank=True) 
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.Customer_Name
	
class Orders(models.Model):
	Order_ID = models.CharField(primary_key=True, max_length=10, blank=True)
	Order_CreateDate = models.CharField(max_length=10, blank=True)
	Order_PickupDate = models.CharField(max_length=10, blank=True)
	Order_PickupStore = models.ForeignKey(Store,on_delete=models.CASCADE)
	Order_ReturnStore = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='+')
	Order_ReturnDate = models.CharField(max_length=10, blank=True)
	Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE, default="1")
	Car_ID = models.ForeignKey(Car, on_delete=models.CASCADE, default="1")
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.Order_ID
		
	class Meta:
		verbose_name_plural = "Orders"

