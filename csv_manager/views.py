from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from csv_manager.serializers import *
from csv_manager.models import StoreLocation, Store
from rest_framework.views import APIView
from rest_framework.response import Response

from csv_manager.utils import save_csv_data
import pandas as pd

class StoreMetaData(APIView):
    # class based view to fetch store information
    def get(self, request, format=None):
        id = request.query_params["zub_id"]
        store = StoreLocation.objects.get(zub_id=id)
        serializer = StoreLocationSerializer(store)
        return Response(serializer.data)

def upload(request):
    if request.method == "GET":
        return render(request, 'csv_manager/index.html')
    
    if request.method == "POST":
        csv_file = request.FILES['file']
        csv_data = pd.read_csv(csv_file).to_dict('r')
        save_csv_data(csv_data)
    
        return render(request, 'csv_manager/index.html')
