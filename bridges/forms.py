from django import forms

from .models import Bridge


class BridgeCreationForm(forms.Form):
    latitude = forms.DecimalField(label='latitude', required=True)
    longitude = forms.DecimalField(label='longitude', required=True)
    height = forms.DecimalField(label='hauteur du pont (m)', required=True)
    width = forms.DecimalField(label='largeur du pont (m)', required=True)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self):
        bridge, created = Bridge.objects.get_or_create(
            user=self.request.user,
            latitude=self.cleaned_data['latitude'],
            longitude=self.cleaned_data['longitude'],
            height=self.cleaned_data['height'],
            width=self.cleaned_data['width'],
        )
        return bridge
