from rest_framework import serializers
from . models import Store, StoreLocation

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['company_id', 'zubale_id', 'determinante',
                  'status', 'cadena', 'formato',
                  'nombre', 'pais', 'cadena_nombre']

class StoreLocationSerializer(serializers.ModelSerializer):
    store = StoreSerializer(many=False)
    class Meta:
        model = StoreLocation
        fields = ['store', 'zub_id', 'zubale_area',
                  'direccion', 'colonia', 'ciudad',
                  'estado', 'zip', 'latitud',
                  'longitud', 'url_google_maps', 'fronterizo',
                  'name_val', 'lat_lon_val']