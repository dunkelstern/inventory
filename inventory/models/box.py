from django.db import models
from .container import CanBeContained, Container


class Box(CanBeContained, Container):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Boxes'