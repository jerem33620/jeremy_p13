from django import forms


class RouteSearchForm(forms.Form):
    origin = forms.CharField(label="Adresse d'origine", required=True)
    destination = forms.CharField(
        label="Adresse de destination", required=True
    )
