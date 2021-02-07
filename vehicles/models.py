import os
from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .managers import VehicleManager


def get_vehicle_path(instance, filename):
    """Computes avatar file path."""
    upload_to = 'vehicles/'
    ext = filename.split('.')[-1]
    filename = f'{instance.owner}-{uuid4().hex}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Vehicle(models.Model):
    TUNNEL_CATEGORIES = (
        ('', _('No tunnel category')),
        ('B', _('Tunnel category B')),
        ('C', _('Tunnel category C')),
        ('D', _('Tunnel category D')),
        ('E', _('Tunnel category E')),
    )
    TRUCK_TYPES = (
        ("C", _("Car")),
        ("S", _("Straight")),
        ("T", _("Tractor")),
    )
    name = models.CharField(
        _("vehicle name"),
        max_length=200,
    )
    gross_weight = models.IntegerField(
        _("vehicle gross weight"),
        blank=True,
        null=True,
    )
    height = models.DecimalField(
        _("vehicle height"),
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    width = models.DecimalField(
        _("vehicle width"),
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    length = models.DecimalField(
        _("vehicle length"),
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    tunnel_category = models.CharField(
        _("vehicle tunnel category"),
        max_length=1,
        choices=TUNNEL_CATEGORIES,
        blank=True,
    )
    truck_type = models.CharField(
        _("vehicle type"),
        max_length=1,
        choices=TRUCK_TYPES,
        default="S",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='vehicle owner',
        on_delete=models.SET_NULL,
        null=True,
        related_name=_("vehicles"),
    )
    created_date = models.DateTimeField(
        _("vehicle creation date"),
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        _("last vehicle update date"),
        auto_now=True,
    )
    image = models.ImageField(
        _("vehicle image"),
        max_length=255,
        upload_to=get_vehicle_path,
        blank=True,
    )

    objects = VehicleManager()

    class Meta:
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")

    def __str__(self):
        return self.name

    def get_truck_info(self):
        if self.truck_type == 'C':
            return {}

        return {
            'grossWeight': self.gross_weight,
            'height': self.height,
            'width': self.width,
            'length': self.length,
            'tunnelCategory': self.tunnel_category,
            'type': self.get_truck_type_display().lower(),
        }