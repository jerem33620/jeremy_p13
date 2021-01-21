from django.db import models
from django.conf import settings


class Vehicle(models.Model):
    height = models.DecimalField(max_digits=3, decimal_places=2)
    width = models.IntegerField()
    length = models.DecimalField(max_digits=3, decimal_places=2)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="vehicles",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_update = models.DateTimeField(auto_now=True)