from django.urls import reverse
from django.db import models
from .container import Container, CanBeContained


class Area(CanBeContained, Container):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    show_sub_area = models.BooleanField(default=True, help_text="Allow sub-areas to be defined in this area")
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return reverse("area-detail", args=[self.pk])

    class Meta:
        ordering = ("name", )
