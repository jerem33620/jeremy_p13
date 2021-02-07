from decimal import Decimal
from unittest.mock import patch, MagicMock
import json

from django.test import TestCase

from routes.utils import search_route


@patch('routes.utils.Bridge.objects.filter')
@patch('routes.utils.RoutingClient')
class RouteUtilsTests(TestCase):
    def test_search_route_calls_api_with_right_params(
        self, MockRoutingClient, mock_bridge_filter
    ):
        mock_vehicle = MagicMock(
            height=Decimal('3.0'), width=Decimal('4.0'), truck_type='S'
        )
        mock_vehicle.get_truck_info.return_value = 'truck info'
        mock_bridge_filter.return_value = []
        search_route('Paris', 'Bordeaux', mock_vehicle)
        mock_get_route = MockRoutingClient.return_value.get_route
        mock_get_route.assert_called_with(
            origin='Paris',
            destination='Bordeaux',
            transportMode='truck',
            return_='polyline',
            truck='truck info',
            avoid_areas=[],
        )
