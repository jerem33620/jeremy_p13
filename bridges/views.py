from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Bridge


class BridgeCreate(CreateView):
    template_name = 'bridges/register.html'
    model = Bridge
    fields = (
        'latitude',
        'longitude',
        'height',
        'width',
    )

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'bridges/register.html', {'form': form})
