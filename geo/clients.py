import re
import os

import requests

from .utils import get_bounding_box_string


class HereApiError(Exception):
    pass


class Position:
    """Reprsents a position (GPS and address)."""

    def __init__(self, address, latitude, longitude):
        """Initializes a new position."""
        self.address = address
        self.latitude = latitude
        self.longitude = longitude

    @property
    def coordinates(self):
        """Latitude and longitude as a tuple."""
        return self.latitude, self.longitude

    def __repr__(self):
        return f"{self.address} ({self.latitude}, {self.longitude})"


class GeocodingClient:
    """Represents a client to Here.com geocoding API."""

    def __init__(self, key=None):
        """Initializes the geocoding client."""
        self._key = key or os.environ['HERE_API_KEY']

    def geosearch(self, place):
        """Searches the text on here.com geocoding api and returns address
        GPS coordinates."""
        url = 'https://geocode.search.hereapi.com/v1/geocode'
        params = {'q': place, 'apiKey': self._key}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException:
            raise HereApiError("Request to Here.com API failed")
        data = response.json()
        item = data.get('items')[0]
        return Position(
            address=item.get('address'),
            latitude=item.get('position', {}).get('lat'),
            longitude=item.get('position', {}).get('lng'),
        )


class RoutingClient:
    """Represents a client to Here.com route API."""

    def __init__(self, key=None):
        self._key = key or os.environ['HERE_API_KEY']
        self._geocoder = GeocodingClient(self._key)

    def _get_coordinates(self, place):
        """Recovers GPS coordinates of the given place if not already
        coordinates."""
        if re.match(r"-?[\d.]+,-?[\d.]+", place):
            return tuple(place.split(","))
        return tuple(
            str(coord) for coord in self._geocoder.geosearch(place).coordinates
        )

    def get_route(
        self,
        origin,
        destination,
        transportMode='car',
        return_='polyline',
        truck=None,
        avoid_features=None,
        avoid_areas=None,
        lang='fr',
    ):
        origin = self._get_coordinates(origin)
        destination = self._get_coordinates(destination)
        url = 'https://router.hereapi.com/v8/routes'
        params = {
            'origin': ",".join(origin),
            'destination': ",".join(destination),
            'apiKey': self._key,
            'transportMode': transportMode,
            'return': return_,
        }

        # Handle truck parameters
        if transportMode == 'truck' and isinstance(truck, dict):
            if truck.get('grossWeight'):
                params['truck[grossWeight]'] = truck['grossWeight']
            if truck.get('height'):
                params['truck[height]'] = truck['height']
            if truck.get('width'):
                params['truck[width]'] = truck['width']
            if truck.get('length'):
                params['truck[length]'] = truck['length']
            if truck.get('tunnelCategory'):
                params['truck[tunnelCategory]'] = truck['tunnelCategory']
            if truck.get('type'):
                params['truck[type]'] = truck['type']

        # Handle things to avoid
        if isinstance(avoid_features, list) and avoid_features:
            params['avoid[features]'] = ",".join(avoid_features)

        if isinstance(avoid_areas, list) and avoid_areas:
            params['avoid[areas]'] = "|".join(avoid_areas)
        print(params)
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.RequestException:
            raise HereApiError("Request to Here.com API failed")
        return response.json()