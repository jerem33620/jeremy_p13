from django.urls import path

from .views import VehicleCreate

app_name = 'vehicles'

urlpatterns = [
    path('', VehicleCreate.as_view(), name='create')
]