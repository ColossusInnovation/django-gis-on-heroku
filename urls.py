from django.urls import path
from django.contrib.gis import admin

urlpatterns = [
    path(r'admin/', admin.site.urls)
]
