from django.db import models

class Store(models.Model):
    company_id = models.CharField(max_length=50)
    zubale_id = models.IntegerField()
    determinante = models.IntegerField()
    status = models.BooleanField()
    cadena = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    cadena_nombre = models.CharField(max_length=50)

class StoreLocation(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    zub_id = models.IntegerField()
    zubale_area = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    colonia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    zip = models.IntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    url_google_maps = models.CharField(max_length=200)
    fronterizo = models.BooleanField()
    name_val = models.IntegerField()
    lat_lon_val = models.IntegerField()