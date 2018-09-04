#Lydya source file

from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from crcapp.models import Car,Orders,Store,Customer
from pytz import UTC


DATETIME_FORMAT = '%d/%m/%Y %H:%M'


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the carRental data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
	help = "Loads data from carRentalDataSource.csv into our carRental model"

	def handle(self, *args, **options):
		if Car.objects.exists():
			print('Car data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		for row in DictReader(open('./CarRentalDataSource.csv')):
			car = Car()
			car.Car_ID = row['Car_ID']
			car.save()

			car.Car_MakeName = row['Car_MakeName']
			car.Car_Model = row['Car_Model']
			car.Car_Series = row['Car_Series']
			car.Car_SeriesYear = row['Car_SeriesYear']
			car.Car_PriceNew = row['Car_PriceNew']
			raw_Car_EngineSize = row['Car_EngineSize']
			Car_EngineSize = raw_Car_EngineSize[:-1]
			car.Car_EngineSize = Car_EngineSize

			car.Car_FuelSystem = row['Car_FuelSystem']
			raw_Car_TankCapacity = row['Car_TankCapacity']
			Car_TankCapacity = raw_Car_TankCapacity[:-1]
			
			if Car_TankCapacity == 'NUL':
				Car_TankCapacity = 0
			Car_TankCapacity = float(Car_TankCapacity)
			car.Car_TankCapacity = Car_TankCapacity
			car.Car_Power = row['Car_Power']
			car.Car_SeatingCapacity = row['Car_SeatingCapacity']
			car.Car_StandardTransmission = row['Car_StandardTransmission']
			car.Car_BodyType = row['Car_BodyType']
			car.Car_Drive = row['Car_Drive']
			car.Car_Wheelbase = row['Car_Wheelbase']

			car.save()
		
		if Store.objects.exists():
			print('Store data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		for row in DictReader(open('./CarRentalDataSource.csv')):
			
			store = Store()
			
			store.Store_ID = row['Order_PickupStore']
			store.Store_Name = row['Pickup_Store_Name']
			store.Store_Address = row['Pickup_Store_Address']
			store.Store_Phone = row['Pickup_Store_Phone']
			store.Store_City = row['Pickup_Store_City']
			store.Store_State = row['Pickup_Store_State_Name']
			
			store.save()
			
			
		for row in DictReader(open('./CarRentalDataSource.csv')):
			
			store = Store()
			
			store.Store_ID = row['Order_ReturnStore']
			store.Store_Name = row['Return_Store_Name']
			store.Store_Address = row['Return_Store_Address']
			store.Store_Phone = row['Return_Store_Phone']
			store.Store_City = row['Return_Store_City']
			store.Store_State = row['Return_Store_State']
			
			store.save()
			
		if Customer.objects.exists():
			print('Customer data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		for row in DictReader(open('./CarRentalDataSource.csv')):
			
			customer = Customer()
	
			customer.Customer_ID = row['Customer_ID']
			customer.Customer_Name = row['Customer_Name']
			customer.Customer_Phone = row['Customer_Phone']
			customer.Customer_Addresss = row['Customer_Addresss']
			customer.Customer_Brithday = row['Customer_Brithday']
			customer.Customer_Occupation = row['Customer_Occupation']
			customer.Customer_Gender = row['Customer_Gender']
			
			customer.save()
			
					
		if Orders.objects.exists():
			print('Orders data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		for row in DictReader(open('./CarRentalDataSource.csv')):
			
			orders = Orders()
			
			orders.Order_ID = row['Order_ID']
			orders.Order_CreateDate = row['Order_CreateDate']
			orders.Order_PickupDate = row['Order_PickupDate']
			orders.Order_PickupStore = Store.objects.filter(Store_ID=row['Order_PickupStore'])[0]
			orders.Order_ReturnStore = Store.objects.filter(Store_ID=row['Order_ReturnStore'])[0]
			
			orders.Order_ReturnDate = row['Order_ReturnDate']
			orders.Customer_ID = Customer.objects.filter(Customer_ID=row['Customer_ID'])[0]
			orders.Car_ID = Car.objects.filter(Car_ID=row['Car_ID'])[0]
			
			orders.save()
		
		
		