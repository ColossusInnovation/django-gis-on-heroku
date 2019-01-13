# django-gis-on-heroku

## Heroku Setup

This used to be quite the pain. Now you just need to set `BUILD_WITH_GEO_LIBRARIES=1` in your Heroku environment before
building your project. The default Python buildpack will build the needed GDAL and GEOS libraries on the container that
runs your application. 

## Django Settings Changes

1. Add `'django.contrib.gis'` to your `INSTALLED_APPS`
2. Change your `DATABASES` dict to use postgis, like so:

```python
 DATABASES['default'] = dj_database_url.config(conn_max_age=600,
                                               default='postgis://localhost:5432/{}'.format(APP_NAME))
 # VERY IMPORTANT BECAUSE HEROKU WILL USE 'postgres' AS THE SCHEME
 DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
```

## Other Django Things

1. In `urls.py`, change `from django.contrib import admin` to 
`from django.contrib.gis import admin` for admin urls
2. In whatever app makes sense, add the following migration:

```python
from django.contrib.postgres.operations import CreateExtension
from django.db import migrations


class Migration(migrations.Migration):
    operations = [
        CreateExtension('postgis') # base postgis functionality
        # CreateExtension('postgis_topology') # if you need the additional topology functionality
    ]
```
