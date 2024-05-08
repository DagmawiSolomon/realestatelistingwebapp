from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from django.contrib.gis.db import models as gismodel
from mapwidgets.widgets import MapboxPointFieldWidget
from .models import (Listing,Property,Amenities)
# Register your models here.



admin.site.register(Amenities)
admin.site.register(Listing)

class PropertyAdmin(gisadmin.ModelAdmin):
    formfield_overrides = {
        gismodel.PointField: {"widget": MapboxPointFieldWidget}
    }

admin.site.register(Property, PropertyAdmin)