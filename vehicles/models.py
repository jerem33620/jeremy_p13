import os
from uuid import uuid4

from django.db import models
from django.conf import settings


def get_vehicle_path(instance, filename):
    """Computes avatar file path."""
    upload_to = 'vehicles/'
    ext = filename.split('.')[-1]
    filename = f'{instance.creator}-{uuid4().hex}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Vehicle(models.Model):
    TUNNEL_CATEGORIES = (
        ('A', 'Tunnel category A'),
        ('B', 'Tunnel category B'),
        ('C', 'Tunnel category C'),
        ('D', 'Tunnel category D'),
        ('E', 'Tunnel category E'),
    )
    TRUCK_TYPES = (
        ("S", "Straight"),
        ("T", "Tractor"),
    )
    name = models.CharField(
        "vehicle name",
        max_length=200,
        blank=None,
        null=True,
    )
    gross_weight = models.IntegerField(
        "vehicle gross weight",
        blank=True,
        null=True,
    )
    height = models.DecimalField(
        "vehicle height",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    width = models.DecimalField(
        "vehicle width",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    length = models.DecimalField(
        "vehicle length",
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True,
    )
    has_hazardous_goods = models.BooleanField(
        'has hazardous goods',
        default=False,
    )
    tunnel_category = models.CharField(
        "vehicle tunnel category",
        max_length=1,
        choices=TUNNEL_CATEGORIES,
        default="A",
    )
    truck_type = models.CharField(
        "vehicle type",
        max_length=1,
        choices=TRUCK_TYPES,
        default="S",
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="vehicles",
    )
    created_date = models.DateTimeField(
        "vehicle creation date",
        auto_now_add=True,
    )
    updated_update = models.DateTimeField(
        "last vehicle update date",
        auto_now=True,
    )
    image = models.ImageField(
        max_length=255, upload_to=get_vehicle_path, blank=True
    )
