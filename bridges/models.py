from django.db import models
from django.conf import settings

from .managers import BridgeManager
from django.utils.translation import gettext_lazy as _


class Bridge(models.Model):
    height = models.DecimalField(
        _('bridge height'),
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    width = models.DecimalField(
        _('bridge width'),
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    latitude_north = models.DecimalField(
        _('bounding box north latitude'),
        max_digits=10,
        decimal_places=7,
    )
    latitude_south = models.DecimalField(
        _('bounding box south latitude'),
        max_digits=10,
        decimal_places=7,
    )
    longitude_west = models.DecimalField(
        _('bounding box west longitude'),
        max_digits=10,
        decimal_places=7,
    )
    longitude_east = models.DecimalField(
        _('bounding box east longitude'),
        max_digits=10,
        decimal_places=7,
    )
    latitude = models.DecimalField(
        _('bounding box center latitude'),
        max_digits=10,
        decimal_places=7,
    )
    longitude = models.DecimalField(
        _('bounding box center longitude'),
        max_digits=10,
        decimal_places=7,
    )
    created_date = models.DateTimeField(
        _('date of creation'),
        auto_now_add=True,
    )
    last_update = models.DateTimeField(
        _('date of last update'),
        auto_now=True,
    )
    contributors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('bridge contributors'),
        related_name="bridges",
        through='BridgeUpdate',
    )

    objects = BridgeManager()

    class Meta:
        verbose_name = _("bridge")
        verbose_name_plural = _("bridges")

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"

    @property
    def bbox(self):
        """Dictionary representation of the bounding box."""
        return [
            self.longitude_west,
            self.latitude_south,
            self.longitude_east,
            self.latitude_north,
        ]

    @bbox.setter
    def bbox(self, values):
        self.longitude_west = values[0]
        self.latitude_south = values[1]
        self.longitude_east = values[2]
        self.latitude_north = values[3]

    @property
    def bbox_string(self):
        """String representation of the bounding box."""
        return (
            f"bbox:{self.longitude_west:.7f},{self.latitude_south:.7f},"
            f"{self.longitude_east:.7f},{self.latitude_north:.7f}"
        )


class BridgeUpdate(models.Model):
    contributor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('update contributor'),
        on_delete=models.CASCADE,
        related_name="bridge_updates",
    )
    bridge = models.ForeignKey(
        'Bridge',
        verbose_name=_('updated bridge'),
        on_delete=models.CASCADE,
        related_name="bridge_updates",
    )
    updated_date = models.DateTimeField(auto_now_add=True)
