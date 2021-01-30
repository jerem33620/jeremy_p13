import math

# Semi-axes of WGS-84 geoidal reference
EARTH_RADIUS_EQUATOR = 6378137.0
EARTH_RADIUS_POLE = 6356752.3


def deg2rad(degrees):
    """Converts an angle from degrees to radians."""
    return math.pi * degrees / 180.0


def rad2deg(radians):
    """Converts an angle from radians to degrees."""
    return 180.0 * radians / math.pi


def get_earth_radius(latitude):
    """Computes earth radius as a function of the latitude.
    From:  http://en.wikipedia.org/wiki/Earth_radius"""
    a_n = EARTH_RADIUS_EQUATOR ** 2 * math.cos(latitude)
    b_n = EARTH_RADIUS_POLE ** 2 * math.sin(latitude)
    a_d = EARTH_RADIUS_EQUATOR * math.cos(latitude)
    b_d = EARTH_RADIUS_POLE * math.sin(latitude)
    return math.sqrt((a_n ** 2 + b_n ** 2) / (a_d ** 2 + b_d ** 2))


def get_bounding_box(latitude_deg, longitude_deg, half_side_meters):
    """Computes a bounding box surrounding the point at given coordinates,
    assuming local approximation of Earth surface as a sphere of radius given
    by WGS84.
    Returns:
        dictionary west longitude, south latitude, east longitude,
        north latitude
    """
    lat = deg2rad(latitude_deg)
    lng = deg2rad(longitude_deg)

    # Radius of Earth at given latitude
    radius = get_earth_radius(lat)
    # Radius of the parallel at given latitude
    pradius = radius * math.cos(lat)

    lat_south = lat - half_side_meters / radius
    lat_north = lat + half_side_meters / radius
    lng_west = lng - half_side_meters / pradius
    lng_east = lng + half_side_meters / pradius

    return {
        'longitude_west': rad2deg(lng_west),
        'latitude_south': rad2deg(lat_south),
        'longitude_east': rad2deg(lng_east),
        'latitude_north': rad2deg(lat_north),
    }


def get_bounding_box_string(latitude_deg, longitude_deg, half_side_meters):
    """Computes a bounding box surrounding the point at given coordinates,
    assuming local approximation of Earth surface as a sphere of radius given
    by WGS84.
    Returns:
        bbox string of the form bbox:{west},{south},{east},{north}
    """
    coordinates = get_bounding_box(
        latitude_deg, longitude_deg, half_side_meters
    )
    return f"bbox:{','.join(coordinates.values)}"