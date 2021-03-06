"""Models file."""

from django.utils.timezone import now
from django.db import models


class Urls(models.Model):
    """Class Urls."""

    full_path = models.TextField()
    short_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=now())

    objects = models.Manager()
