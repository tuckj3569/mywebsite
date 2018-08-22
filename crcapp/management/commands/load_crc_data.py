#Lydya source file

from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from crcapp.models import Car, Orders,Store,Customer
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
		if Car.objects.exists() or Orders.objects.exists():
			print('Pet data already loaded...exiting.')
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
