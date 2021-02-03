import os
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def get_avatar_path(instance, filename):
    """Computes avatar file path."""
    upload_to = 'avatars'
    ext = filename.split('.')[-1]
    filename = f'{instance.username}-{uuid4().hex}.{ext}'
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class User(AbstractUser):
    """Model representing the website users."""

    avatar = models.ImageField(
        _('user avatar'), max_length=255, upload_to=get_avatar_path, blank=True
    )
