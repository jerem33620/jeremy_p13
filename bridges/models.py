from django.db import models
from django.conf import settings


class Bridge(models.Model):
    height = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    width = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    longitute = models.DecimalField(
        max_digits=10,
        decimal_places=7,
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="bridges",
    )
    last_contributor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="bridges",
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    last_update = models.DateTimeField(
        auto_now=True,
    )

class Assobridge(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    bridge = models.ForeignKey(
        Bridge,
        on_delete=models.CASCADE,
    )
    update_date = models.DateTimeField(
        auto_now_add=True,
    )