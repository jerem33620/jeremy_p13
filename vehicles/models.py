import os
from uuid import uuid4

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def get_vehicle_path(instance, filename):
    """Computes avatar file path."""
    upload_to = 'vehicles/'
    ext = filename.split('.')[-1]
    filename = f'{instance.owner}-{uuid4().hex}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Vehicle(models.Model):
    TUNNEL_CATEGORIES = (
        ('X', _('No tunnel category')),
        ('A', _('Tunnel category A')),
        ('B', _('Tunnel category B')),
        ('C', _('Tunnel category C')),
        ('D', _('Tunnel category D')),
        ('E', _('Tunnel category E')),
    )
    TRUCK_TYPES = (
        ("C", _("Car")),
        ("S", _("Straight truck")),
        ("T", _("Tractor truck")),
    )
    name = models.CharField(
        _("vehicle name"),
        max_length=200,
        blank=None,
        null=True,
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
    has_hazardous_goods = models.BooleanField(
        _('has hazardous goods'),
        default=False,
    )
    tunnel_category = models.CharField(
        _("vehicle tunnel category"),
        max_length=1,
        choices=TUNNEL_CATEGORIES,
        default="X",
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
        related_name="vehicles",
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

    class Meta:
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")

    def __str__(self):
        return self.name
