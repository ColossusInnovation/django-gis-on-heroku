from django.contrib.gis import admin
from .models import GeographicThing

admin.site.register(GeographicThing, admin.GeoModelAdmin)
