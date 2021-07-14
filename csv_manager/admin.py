from django.contrib import admin
from . models import Store, StoreLocation

admin.site.register([StoreLocation, Store])
