import io

from django import forms
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from .models import Vehicle


class VehicleChangeForm(forms.ModelForm):
    """Form responsible of getting updated info for a vehicle."""

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
    """From responsible for handling the upload of a new vehicle image."""

    image = forms.FileField(required=False)
    x = forms.FloatField(required=False, widget=forms.HiddenInput())
    y = forms.FloatField(required=False, widget=forms.HiddenInput())
    image_width = forms.FloatField(required=False, widget=forms.HiddenInput())
    image_height = forms.FloatField(required=False, widget=forms.HiddenInput())

    def save(self, pk, commit=True):
        """Crops, resize and crop the newly uploaded image."""
        vehicle = Vehicle.objects.get(pk=pk)
        if self.cleaned_data.get('image'):
            image = self.cleaned_data.get('image')
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            width = self.cleaned_data.get('image_width')
            height = self.cleaned_data.get('image_height')

            if x is not None:
                img = Image.open(io.BytesIO(image.read()))
                cropped_img = img.crop((x, y, x + width, y + height))
                resized_img = cropped_img.resize(
                    settings.USER_AVATAR_SIZE, Image.ANTIALIAS
                )
                buffer = io.BytesIO()
                resized_img.save(buffer, format=img.format)
                image = SimpleUploadedFile(
                    image.name, buffer.getvalue(), image.content_type
                )
            vehicle.image = image
            if commit:
                vehicle.save()

        return vehicle


class VehicleCreationForm(forms.ModelForm):
    """Form responsible of gathering the necessary info to create a new
    vehicle."""

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

    def save(self, commit=True):
        """Saves a new vehicle in database. If an image is uploaded, it is
        cropped and resized."""
        vehicle = super().save(commit=False)
        if self.cleaned_data.get('image'):
            image = self.cleaned_data.get('image')
            x = self.cleaned_data.get('x')
            y = self.cleaned_data.get('y')
            width = self.cleaned_data.get('image_width')
            height = self.cleaned_data.get('image_height')

            if x is not None:
                img = Image.open(io.BytesIO(image.read()))
                cropped_img = img.crop((x, y, x + width, y + height))
                resized_img = cropped_img.resize(
                    settings.USER_AVATAR_SIZE, Image.ANTIALIAS
                )
                buffer = io.BytesIO()
                resized_img.save(buffer, format=img.format)
                image = SimpleUploadedFile(
                    image.name, buffer.getvalue(), image.content_type
                )
            vehicle.image = image
        if commit:
            vehicle.save()

        return vehicle