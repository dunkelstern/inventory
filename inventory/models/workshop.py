from django.urls import reverse
from django.db import models
from .container import Container


class Workshop(Container):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return reverse("workshop-detail", args=[self.pk])
