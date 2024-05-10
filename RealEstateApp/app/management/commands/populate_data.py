from django.core.management.base import BaseCommand, CommandParser
from app.models import Property, Amenities, Listing,Amenities
from accounts.models import Agent,CustomUser
from faker import Faker
import random
from django.contrib.gis.geos import Point
from django.utils import timezone

fake = Faker()


def choose_random(arr)-> str:
    return random.choice(arr)

def generate_property_name() -> str:
    adjectives = ['cozy', 'spacious', 'modern', 'rustic', 'luxurious', 'quaint', 'charming', 'elegant', 'serene', 'vibrant', 'stunning', 'majestic', 'picturesque', 'serene', 'secluded', 'breathtaking', 'idyllic', 'panoramic', 'peaceful', 'secluded']
    nouns = ['cottage', 'villa', 'apartment', 'mansion', 'bungalow', 'loft', 'cabin', 'chalet', 'penthouse', 'manor', 'estate', 'retreat', 'hideaway', 'residence', 'lodge', 'palace', 'castle', 'chateau', 'fortress', 'dwelling']

    adjective = choose_random(adjectives)
    noun = choose_random(nouns)
    return f"{adjective} {noun}"


def generate_property_type()->str:
    property_type = ["Single family home","Townhouse","Condominium","Apartment", "Office building", "Retail space", "Industrial property","Land"]
    return choose_random(property_type)

def generate_status()->str:
    statuses = ["active","pending","sold"]
    return choose_random(statuses)

def generate_amenities_title()->str:
    building_amenities = [
    "Swimming pool",
    "Gym/fitness center",
    "Parking garage",
    "Elevator",
    "24/7 Security",
    "Concierge service",
    "Roof deck",
    "Laundry facilities",
    "Pet-friendly",
    "Balcony/patio",
    "Central heating/cooling",
    "WiFi",
    "Storage space",
    "BBQ area",
    "Community lounge",
    "Playground",
    "Tennis courts",
    "Bike storage",
    "Yoga studio",
    "Business center",
    "Conference room",
    "Theater room",
    "Sauna",
    "Jacuzzi/hot tub",
    "On-site maintenance",
    "On-site management",
    "Package service",
    "Green space",
    "Dog park",
    "Electric car charging stations",
    "Library",
    "Catering kitchen",
    "Coffee bar",
    "Game room",
    "Valet service",
    "Dry cleaning service",
    "Guest suites",
    "Car wash station",
    "Dog grooming station"]

    return random.choice(building_amenities)


def generate_amenities()->None:
    title = generate_amenities_title()
    instance = Amenities.objects.create(
        title=title
    )
    instance.save()

def generate_property() ->None:
    longitude = float(fake.longitude())
    latitude = float(fake.latitude())
    available_amenities = Amenities.objects.all()
    try:
        instance = Property.objects.create(
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

        if available_amenities.exists():
            random_number = random.randint(1, 6)
            amenities = available_amenities[:random_number]
            instance.amenities.set(amenities)
            
        return instance
    except Exception as e:
        print(e)




def generate_agent():
    while True:
        username = fake.user_name()
        if not CustomUser.objects.filter(username=username).exists():    
            break
    password=fake.password()
    phonenumber=fake.basic_phone_number()
    email=fake.email()
    try:
        user = CustomUser.objects.create(
            username=username,
            password=password,
            phonenumber=phonenumber,
            email=email
        )
        instance = Agent.objects.create(
            user=user,
            username=username,
            password=password,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            

        )
        return instance
    except Exception as e:
        print(e)

def generate_listing() -> None:
    agent = generate_agent()
    if agent is not None: 
        property_instance = generate_property()
        list_date = timezone.now()
        open_house = timezone.now()
        try:
            instance = Listing.objects.create(
                property=property_instance,
                list_date=list_date,
                agent=agent,
                open_house=open_house,
            )
            return instance
        except Exception as e:
            print(e)





class Command(BaseCommand):
    help = 'Poulate databse with initial data'


    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('model', type=str, help='Enter the model to populate')
        parser.add_argument('count', type=int, help='Number of data entries to populate the table with.')
        
    
    def handle(self,*args, **options):
        model_name = options['model']
        count = options['count']
            
        for _ in range(count):
            if(model_name=="Property"):
                generate_property()
            elif(model_name=="Amenities"):
                generate_amenities()
            elif(model_name=="Listing"):
                generate_listing()
            
        self.stdout.write(self.style.SUCCESS(f'{count} data entries populated successfully'))
    
