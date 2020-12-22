from django.urls import reverse
from django.db import models
from .container import Container


class Workshop(Container):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    show_boxes = models.BooleanField(default=True, help_text="Allow boxes to be defined directly in this workshop")
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return reverse("workshop-detail", args=[self.pk])
