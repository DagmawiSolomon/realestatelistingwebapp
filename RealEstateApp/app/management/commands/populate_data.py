from django.core.management.base import BaseCommand, CommandParser
from app.models import Property
from faker import Faker
import random
from django.contrib.gis.geos import Point

fake = Faker()


def choose_random(arr)-> str:
    return random.choice(arr)

def generate_property_name() -> str:
    adjectives = ['cozy', 'spacious', 'modern', 'rustic', 'luxurious', 'quaint', 'charming', 'elegant', 'serene', 'vibrant', 'stunning', 'majestic', 'picturesque', 'serene', 'secluded', 'breathtaking', 'idyllic', 'panoramic', 'peaceful', 'secluded']
    nouns = ['cottage', 'villa', 'apartment', 'mansion', 'bungalow', 'loft', 'cabin', 'chalet', 'penthouse', 'manor', 'estate', 'retreat', 'hideaway', 'residence', 'lodge', 'palace', 'castle', 'chateau', 'fortress', 'dwelling']

    adjective = choose_random(adjectives)
    noun = choose_random(nouns)
    return f"{adjective} {noun}"

def generate_city_name()->str:
    cities = ["Addis Ababa", "London", "Tokyo", "Nairbo"]
    return choose_random(cities)

def generate_state_province()->str:
    cities = ["Alaska", "Tigray", "Somalia", "DC"]
    return choose_random(cities)

def generate_property_type()->str:
    property_type = ["Single family home","Townhouse","Condominium","Apartment", "Office building", "Retail space", "Industrial property","Land"]
    return choose_random(property_type)

def generate_status()->str:
    statuses = ["active","pending","sold"]
    return choose_random(statuses)


class Command(BaseCommand):
    help = 'Poulate databse with initial data'


    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Number of data entries to populate the table with.')
    
    def handle(self,*args, **options):
        count = options['count']
        for _ in range(count):
            longitude = float(fake.longitude())
            latitude = float(fake.latitude())
            try:
                x = Property.objects.create(
                    title=generate_property_name(),
                    address=fake.street_address(),
                    city=fake.city(),
                    state_province=fake.state(),
                    property_type=generate_property_type(),
                    postal_code=fake.postalcode(),
                    square_footage=fake.random_int(min=25, max=999999),
                    bedrooms=fake.random_int(min=1, max=20),
                    bathrooms=fake.random_int(min=1, max=20),
                    year_built=fake.year(),
                    description=fake.text(),
                    price=fake.random_int(min=100000, max=9999999999),
                    status=generate_status(),

                    location=Point(longitude, latitude),
                )
                x.save()
            except Exception as e:
                print(e)
        self.stdout.write(self.style.SUCCESS(f'{count} data entries populated successfully'))
