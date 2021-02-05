import os
import json
import random

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from flexpolyline import decode

from vehicles.models import Vehicle
from .forms import RouteSearchForm
from .utils import search_route


class RouteSearchView(LoginRequiredMixin, TemplateView):
    template_name = 'routes/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RouteSearchForm(self.request.user)
        return context


class RouteResultView(LoginRequiredMixin, TemplateView):
    template_name = 'routes/result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle = self.request.GET.get('vehicle')
        if vehicle:
            vehicle = Vehicle.objects.get_own_vehicle_or_none(
                self.request.user, vehicle
            )
        route = search_route(
            origin=self.request.GET.get('origin'),
            destination=self.request.GET.get('destination'),
            vehicle=vehicle,
        )
        waypoints = None
        if route['routes']:
            waypoints = decode(route['routes'][0]['sections'][0]['polyline'])
            # Here deep linking support a maximum of 18 waypoints
            indexes = sorted(
                random.sample(
                    range(1, len(waypoints) - 1), min(18, len(waypoints) - 2)
                )
            )
            waypoints = "/".join(
                f"{lat:.7f},{lng:.7f}"
                for lat, lng in waypoints[:1]
                + [waypoints[i] for i in indexes]
                + waypoints[-1:]
            )
        print(json.dumps(route))
        return {
            **context,
            'route': json.dumps(route),
            'here_key': os.getenv('HERE_JS_API_KEY'),
            'waypoints': waypoints,
        }
