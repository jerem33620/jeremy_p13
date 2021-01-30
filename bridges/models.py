from django.db import models
from django.conf import settings

from geo.utils import get_bounding_box


class BridgeManager(models.Manager):
    """Manager responsible to handle bridge search and creation."""

    def get_or_create(
        self, latitude, longitude, user, height=None, width=None
    ):
        """Records a new bridge if not already in the database."""
        bounding_box = get_bounding_box(
            latitude, longitude, settings.BOUNDING_BOX_HALF_SIDE
        )
        created = False
        try:
            # Search bridges whose bounding box include latitude and longitude
            bridge = self.model.object.filter(
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
            bridge = self.model.object.create(
                latitude=latitude,
                longitude=longitude,
                height=height,
                width=width,
                **bounding_box,
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
        bridge.users.add(user)

        bridge.save()
        return bridge, created


class Bridge(models.Model):
    height = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    width = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    latitude_north = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    latitude_south = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    longitude_west = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    longitude_east = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    last_update = models.DateTimeField(
        auto_now=True,
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="bridges",
        through='BridgeUpdate',
    )

    objects = BridgeManager()

    class Meta:
        verbose_name = "bridge"
        verbose_name_plural = "bridges"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"

    @property
    def bbox(self):
        """Dictionary representation of the bounding box."""
        return {
            'longitude_west': self.longitude_west,
            'latitude_south': self.latitude_south,
            'longitude_east': self.longitude_east,
            'latitude_north': self.latitude_north,
        }

    @bbox.setter
    def bbox(self, value):
        self.longitude_west = value['longitude_west']
        self.latitude_south = value['latitude_south']
        self.longitude_east = value['longitude_east']
        self.latitude_north = value['latitude_north']

    @property
    def bbox_string(self):
        """String representation of the bounding box."""
        return (
            f"bbox:{self.longitude_west},{self.latitude_south},"
            f"{self.longitude_east},{self.latitude_north}"
        )


class BridgeUpdate(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bridge_updates",
    )
    bridge = models.ForeignKey(
        'Bridge', on_delete=models.CASCADE, related_name="bridge_updates"
    )
    updated_date = models.DateTimeField(auto_now_add=True)
