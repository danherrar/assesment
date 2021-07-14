import math
from csv_manager.models import Store, StoreLocation

def save_csv_data(csv_data):
    
    store_location_keys = ['Zubale Area', 'ZUBID', 'Dirección', 
                           'Colonia', 'Ciudad', 'Estado', 
                           'Zip', 'Latitud', 'Longitud', 
                           'URL Google Maps', 'FRONTERIZO', 'NAME/VAL', 'LAT/LON(VAL)']

    store_keys = ['Company ID', 'Zubale ID', 'Determinante', 
                  'Status', 'Cadena', 'Formato', 
                  'Nombre', 'País', 'CADENA/NOMBRE']

    store = {
             'Company ID': None,
             'Zubale ID': None,
             'Determinante': None,
             'Status': None,
             'Cadena': None,
             'Formato': None,
             'Nombre': None,
             'País': None,
             'CADENA/NOMBRE': None
            }

    store_location = {
                      'store': None,
                      'Zubale Area': None,
                      'ZUBID': None,
                      'Dirección': None,
                      'Colonia': None,
                      'Ciudad': None,
                      'Estado': None,
                      'Zip': None,
                      'Latitud': None,
                      'Longitud': None,
                      'URL Google Maps': None,
                      'FRONTERIZO': None,
                      'NAME/VAL': None,
                      'LAT/LON(VAL)': None
                      }
                
    stores = []            
    store_locations = []

    for store_data in csv_data:
        # creating a copy to avoid reference the same dict while modifying and appending
        s = store.copy()
        sl = store_location.copy()
        for key, value in store_data.items():
            if key in store_keys:
                s[key] = value 
            elif  key in store_location_keys:
                sl[key] = value
    
        stores.append(s)
        store_locations.append(sl)
       
    # for each store saved, a store_location object will be saved
    position = 0
    for st in stores:
        # each store and store_location are at the same index in the in both lists (stores, store_locations)
        # so, first is saving store 
        
        # parsing store values 
        if st['Status'] == 'Activa':
            st['Status'] = True
        elif st['Status'] == 'Inactiva':
            st['Status'] = False

        if math.isnan(st['Determinante']):
            st['Determinante'] = 0
        else:
            st['Determinante'] = int(st['Determinante'])  

        store_obj = Store.objects.create(**{'company_id':st['Company ID'], 'zubale_id':st['Zubale ID'], 'determinante':st['Determinante'], 
                                            'status':st['Status'], 'cadena':st['Cadena'], 'formato':st['Formato'], 
                                            'nombre':st['Nombre'], 'pais':st['País'], 'cadena_nombre':st['CADENA/NOMBRE']})
        
        # and with store_obj fill the one to one relationship at store field in store_locations
        store_locations[position]['store'] = store_obj
        
        # parsing StoreLocation values 
        if store_locations[position]['FRONTERIZO'] == 'NO':
            store_locations[position]['FRONTERIZO'] = False
        elif store_locations[position]['FRONTERIZO'] == 'SI':
            store_locations[position]['FRONTERIZO'] =  True
        
        if math.isnan(store_locations[position]['Zip']):
            store_locations[position]['Zip'] = 0
        else:
            store_locations[position]['Zip'] = int(store_locations[position]['Zip'])

        position += 1 # filling up the next store field 
        
    # creating all the StoreLocation obj to save them all at once with a single query
    StoreLocation.objects.bulk_create([StoreLocation(store=store_location['store'], zub_id=store_location['ZUBID'], zubale_area=store_location['Zubale Area'], 
                                                     direccion=store_location['Dirección'], colonia=store_location['Colonia'], latitud=store_location['Latitud'], 
                                                     longitud=store_location['Longitud'], zip=store_location['Zip'], url_google_maps=store_location['URL Google Maps'],
                                                     fronterizo=store_location['FRONTERIZO'], name_val=store_location['NAME/VAL'], lat_lon_val=store_location['LAT/LON(VAL)'],
                                                     ciudad=store_location['Ciudad'], estado=store_location['Estado']) for store_location in store_locations])
    