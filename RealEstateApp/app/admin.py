from django.contrib import admin
from .models import (Listing,Property,Amenities)
# Register your models here.



admin.site.register(Amenities)
admin.site.register(Listing)
admin.site.register(Property)