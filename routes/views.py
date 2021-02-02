import os
import json

from django.shortcuts import render

from geo.clients import RoutingClient
from .forms import RouteSearchForm


def route_search(request):
    form = RouteSearchForm()
    return render(request, 'routes/search.html', {'form': form})


def route_result(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    client = RoutingClient()
    route = client.get_route(origin, destination)
    return render(
        request,
        'routes/result.html',
        {
            'route': json.dumps(route),
            'origin': origin,
            'destination': destination,
            'here_key': os.getenv('HERE_JS_API_KEY'),
        },
    )
