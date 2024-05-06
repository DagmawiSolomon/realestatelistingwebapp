from django.db import models
from django.contrib.gis.db import models as geomodel
from django.contrib.gis.geos import Point



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

class Property(models.Model):
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
    location = geomodel.PointField(geography=True, default=Point(0.0,0.0))

    def __str__(self) -> str:
        return f"{self.property_type} in {self.address}"
    
