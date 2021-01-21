from django.db import models
from django.conf import settings

from users.models import User


class Vehicule(models.Model):
    height = models.DecimalField(max_digits=3, decimal_places=2)
    width = models.IntegerField()
    length = models.DecimalField(max_digits=3, decimal_places=2)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="vehicules")
    update = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Assovehicule")
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Assovehicule(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now_add=True)