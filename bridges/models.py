from django.db import models
from django.conf import settings

from users.models import User


class Bridge(models.Model):

    height = models.DecimalField(max_digits=3, decimal_places=2)
    width = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitute = models.DecimalField(max_digits=9, decimal_places=6)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="bridges")
    update = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Assobridge")
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Assobridge(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bridge = models.ForeignKey(Bridge, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now_add=True)