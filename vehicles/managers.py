from django.db import models


class VehicleManager(models.Manager):
    def get_own_vehicle_or_none(self, user, pk):
        try:
            vehicle = self.get(owner=user, pk=(pk or 0))
        except self.DoesNotExist:
            vehicle = None
        return vehicle
