from django.contrib.gis.geos import Polygon, MultiPolygon
from django.test import TestCase

from .models import GeographicThing


class DemoAppTests(TestCase):
    def test_can_create_geographic_thing(self):
        p1 = Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))
        p2 = Polygon(((1, 1), (1, 2), (2, 2), (1, 1)))
        mp = MultiPolygon(p1, p2)
        GeographicThing.objects.create(mpoly=mp)
        self.assertEqual(GeographicThing.objects.count(), 1)
