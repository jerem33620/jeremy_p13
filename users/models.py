from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    """ Cette class sert à utiliser AbstractUser pour obtenir tous ce qu'il nous faut pour un utilisateur """
    pass