from decimal import Decimal

from vehicles.models import Vehicle
from bridges.models import Bridge
from geo.clients import RoutingClient


def search_route(origin, destination, vehicle):
    """Seaches a route using the HERE API."""
    client = RoutingClient()
    search_params = {}
    bridges = []
    if vehicle and vehicle.height:
        search_params['height__gt'] = vehicle.height * Decimal('1.1')
    if vehicle and vehicle.width:
        search_params['width__gt'] = vehicle.width * Decimal('1.1')
    if search_params:
        bridges = Bridge.objects.filter(**search_params)
    return client.get_route(
        origin=origin,
        destination=destination,
        transportMode=(
            'car' if not vehicle or vehicle.truck_type == 'C' else 'truck'
        ),
        return_='polyline',
        truck=(
            None
            if not vehicle or vehicle.truck_type == 'C'
            else vehicle.get_truck_info()
        ),
        avoid_areas=[bridge.bbox_string for bridge in bridges],
    )
