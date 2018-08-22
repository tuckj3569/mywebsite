#Lydya source file

from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import CarRental, Vaccine
from pytz import UTC


DATETIME_FORMAT = '%d/%m/%Y %H:%M'

VACCINES_NAMES = [
    'Canine Parvo',
    'Canine Distemper',
    'Canine Rabies',
    'Canine Leptospira',
    'Feline Herpes Virus 1',
    'Feline Rabies',
    'Feline Leukemia'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the CarRental data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from CarRentalDataSource.csv into our CarRental model"

    def handle(self, *args, **options):
        if Car.objects.exists() or Orders.objects.exists() or Store.objects.exists() or Customer.objects.exists():
            print('CarRental data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        for row in DictReader(open('./CarRentalDataSource.csv')):
			Car = Car()
			Car.Car_ID = row['Car_ID']
			Car.Car_MakeName = row['Car_MakeName']
			Car.Car_Model = row['Car_Model']
			Car.Car_Series = row['Car_Series']
			Car.Car_SeriesYear = row['Car_SeriesYear']
			Car.Car_PriceNew = row['Car_PriceNew']
			Car.Car_EngineSize = row['Car_EngineSize']
			Car.Car_FuelSystem = row['Car_FuelSystem']
			Car.Car_TankCapacity = row['Car_TankCapacity']
			Car.Car_Power = row['Car_Power']
			Car.Car_SeatingCapacity = row['Car_SeatingCapacity']
			Car.Car_StandardTransmission = row['Car_StandardTransmission']
			Car.Car_BodyType = row['Car_BodyType']
			Car.Car_Drive = row['Car_Drive']
			Car.Car_Wheelbase = row['Car_Wheelbase']
			
			
			
			
            raw_submission_date = row['submission date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            CarRental.submission_date = submission_date
            CarRental.save()
            raw_vaccination_names = row['vaccinations']
            vaccination_names = [name for name in raw_vaccination_names.split('| ') if name]
            for vac_name in vaccination_names:
                vac = Vaccine.objects.get(name=vac_name)
                CarRental.vaccinations.add(vac)
            CarRental.save()
