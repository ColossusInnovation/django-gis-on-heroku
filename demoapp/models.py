from django.contrib.gis.db import models


class GeographicThing(models.Model):
    mpoly = models.MultiPolygonField()
