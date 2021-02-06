from django.db import models
from django.conf import settings

from geo.utils import get_bounding_box


class BridgeManager(models.Manager):
    """Manager responsible to handle bridge search and creation."""

    def get_or_create(self, user, latitude, longitude, height, width):
        """Records a new bridge if not already in the database."""
        bounding_box = get_bounding_box(
            latitude, longitude, settings.BOUNDING_BOX_HALF_SIDE
        )
        created = False
        try:
            # Search bridges whose bounding box include latitude and longitude
            bridge = self.model.objects.get(
                latitude_north__gt=latitude,
                latitude_south__lt=latitude,
                longitude_west__lt=longitude,
                longitude_east__gt=longitude,
            )
            bridge.latitude = latitude
            bridge.longitude = longitude
            bridge.bbox = bounding_box
        except self.model.DoesNotExist:
            # Create a new bridge, since it does not exist
            bridge = self.model.objects.create(
                latitude=latitude,
                longitude=longitude,
                height=height,
                width=width,
                longitude_west=bounding_box[0],
                latitude_south=bounding_box[1],
                longitude_east=bounding_box[2],
                latitude_north=bounding_box[3],
            )
            created = True

        # Update height and width if new ones are smaller
        if bridge.height is None:
            bridge.height = height
        if bridge.width is None:
            bridge.width = width

        if height and settings.BRIDGE_MIN_HEIGHT <= height <= bridge.height:
            bridge.height = height

        if width and settings.BRIDGE_MIN_WIDTH <= width <= bridge.width:
            bridge.width = width

        # Add user in the update history of the current bright info
        bridge.contributors.add(user)

        bridge.save()
        return bridge, created