from django.db import models
from django.conf import settings

from users.models import User
from vehicles.models import Vehicle
from bridges.models import Bridge


class Favorite(models.Model):
    """ Cette class sert à avoir une table de favoris pour enregistrer
        les utilisateurs, les produits recherchés et les substitues trouvés
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites"
    )
    vehicle = models.ForeignKey(
        "vehicles.Vehicle", on_delete=models.CASCADE, related_name="favorites_as_vehicle"
    )
    bridge = models.ForeignKey(
        "bridges.Bridge", on_delete=models.CASCADE, related_name="favorites_as_bridge"
    )