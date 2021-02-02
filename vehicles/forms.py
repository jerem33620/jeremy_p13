from django import forms
from django.conf import settings
from PIL import Image

from .models import Vehicle


class VehicleCreationForm(forms.ModelForm):
    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    width = forms.FloatField(required=False, widget=forms.HiddenInput())
    height = forms.FloatField(required=False, widget=forms.HiddenInput())

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
            'image',
        )

    def save(self):
        super().save()
        if self.cleaned_data.get('image'):
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            width = self.cleaned_data.get('width')
            height = self.cleaned_data.get('height')

            if all((x, y, width, height)):
                image = Image.open(self.image.path)
                cropped_image = image.crop((x, y, x + width, y + height))
                resized_image = cropped_image.resize(
                    settings.VEHICLE_IMAGE_SIZE, Image.ANTIALIAS
                )
                resized_image.save(self.image.path)

        return self