import datetime

from django.db import models


class Urls(models.Model):
    full_path = models.TextField()
    short_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now())

    objects = models.Manager()
