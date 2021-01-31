from django.db import models
from django.conf import settings

from .managers import BridgeManager


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
