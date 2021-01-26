from django import forms

from .models import settings

class VehicleRegisterForm(forms.ModelForm):
    class Meta:
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