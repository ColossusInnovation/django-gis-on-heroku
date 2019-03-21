from django.contrib.gis.db import models

print("Hello")
class GeographicThing(models.Model):
    mpoly = models.MultiPolygonField()
