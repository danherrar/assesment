from django.http import response
from django.test import TestCase, Client
from csv_manager.models import Store, StoreLocation
from django.urls import reverse

class ModelTest(TestCase):
    def test_fields(self):
        store = Store()
        store.company_id = 0
        store.zubale_id = 0
        store.determinante = 0
        store.status = False
        store.cadena = "Test"
        store.formato = "Test"
        store.nombre = "Test"
        store.pais = "Test"
        store.cadena_nombre = "Test"

        store.save()
        store_record_test = Store.objects.get(id=1)     

        store_location = StoreLocation()

        store_location.store = store_record_test
        store_location.zub_id = 0
        store_location.zubale_area = "Test"
        store_location.direccion = "Test"
        store_location.colonia = "Test"
        store_location.ciudad = "Test"
        store_location.estado = "Test"
        store_location.zip = 0
        store_location.latitud = 0
        store_location.longitud = 0
        store_location.url_google_maps = "Test"
        store_location.fronterizo = False
        store_location.name_val = 0
        store_location.lat_lon_val = 0
        
        store_location.save()
        store_location_record_test = StoreLocation.objects.get(id=1)

        self.assertEqual(store_location_record_test, store_location)
        self.assertEqual(store_record_test, store)
        
class ViewsTest(TestCase):
    def test_upload(self):
        client = Client()

        response = client.get(reverse('upload'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'csv_manager/index.html')
