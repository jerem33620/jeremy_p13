from django.urls import path

from .views import VehicleCreate, VehicleList

app_name = 'vehicles'

urlpatterns = [
    path('', VehicleList.as_view(), name='list'),
    path('create/', VehicleCreate.as_view(), name='create'),
]
