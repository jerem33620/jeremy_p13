from django import forms

from vehicles.models import Vehicle


class RouteSearchForm(forms.Form):
    vehicle = forms.ModelChoiceField(required=False, queryset=None)
    origin = forms.CharField(
        label="Adresse d'origine (adresse ou coordonnées GPS)", required=True
    )
    destination = forms.CharField(
        label="Adresse de destination (adresse ou coordonnées GPS)",
        required=True,
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        vehicles = Vehicle.objects.filter(owner=user)
        self.fields['vehicle'].queryset = vehicles
