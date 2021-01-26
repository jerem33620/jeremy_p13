from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Vehicle

class VehicleCreate(CreateView):
    template_name = 'vehicles/register.html'
    model = Vehicle
    fields = (
            'name',
            'gross_weight',
            'height',
            'width',
            'length',
            'has_hazardous_goods',
            'tunnel_category',
            'truck_type',
        )