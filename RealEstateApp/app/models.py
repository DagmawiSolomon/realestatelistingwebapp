from django.db import models
from django.contrib.gis.db import models as gismodel
from django.contrib.gis.geos import Point
from accounts.models import Agent



property_types = (
    ("Single family home", "Single family home"),
    ("Townhouse", "Townhouse"),
    ("Condominium", "Condominium"),
    ("Apartment", "Apartment"),
    ("Office building", "Office building"),
    ("Retail space", "Retail space"),
    ("Industrial property", "Industrial property"),
    ("Land", "Land"),
)

status_choices = (
    ("active", "active"),
    ("pending", "pending"),
    ("sold", "sold"),
)


class Amenities(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Amenities"
    def __str__(self) -> str:
        return self.title;

class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255, verbose_name="state/province")
    property_type = models.CharField(max_length=255,verbose_name="property type", choices=property_types)
    postal_code = models.CharField(max_length=255, verbose_name="zip/postal code")
    square_footage = models.DecimalField(max_digits=20, decimal_places=10,default=0, verbose_name="square footage(in meter squared)")
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    year_built = models.CharField(max_length=4)
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.CharField(choices=status_choices)
    image = models.ImageField(blank=True, null=True)
    location = gismodel.PointField(geography=True, default=Point(9.005401, 38.763611))

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self) -> str:
        return f"{self.title} in {self.address}"
    
class Listing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    list_date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    open_house = models.DateTimeField(blank=True, null=True)
    #Virtual tool_url to be generated

    def __str__(self) -> str:
        return f"{self.property} by {self.agent}"


#Create own app    
# class Rating(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)



