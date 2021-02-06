from django import forms
from django.conf import settings
from PIL import Image

from .models import Vehicle


class VehicleChangeForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = (
            'name',
            'gross_weight',
            'height',
            'width',
            'length',
            'tunnel_category',
            'truck_type',
        )


class VehicleImageChangeForm(forms.Form):
    image = forms.FileField(required=False)
    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    image_width = forms.FloatField(required=False, widget=forms.HiddenInput())
    image_height = forms.FloatField(required=False, widget=forms.HiddenInput())

    def save(self, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        if self.cleaned_data.get('image'):
            vehicle.image = self.cleaned_data.get('image')
            vehicle.save()
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            width = self.cleaned_data.get('image_width')
            height = self.cleaned_data.get('image_height')

            if x is not None:
                image = Image.open(vehicle.image.path)
                cropped_image = image.crop((x, y, x + width, y + height))
                resized_image = cropped_image.resize(
                    settings.VEHICLE_IMAGE_SIZE, Image.ANTIALIAS
                )
                resized_image.save(vehicle.image.path)

        return vehicle


class VehicleCreationForm(forms.ModelForm):
    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    image_width = forms.FloatField(required=False, widget=forms.HiddenInput())
    image_height = forms.FloatField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Vehicle
        fields = (
            'name',
            'gross_weight',
            'height',
            'width',
            'length',
            'tunnel_category',
            'truck_type',
            'image',
        )

    def save(self):
        vehicle = super().save()
        if vehicle.image:
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            width = self.cleaned_data.get('image_width')
            height = self.cleaned_data.get('image_height')

            # if x is not None:
            #     image = Image.open(vehicle.image.path)
            #     cropped_image = image.crop((x, y, x + width, y + height))
            #     resized_image = cropped_image.resize(
            #         settings.VEHICLE_IMAGE_SIZE, Image.ANTIALIAS
            #     )
            #     resized_image.save(vehicle.image.path)

        return self