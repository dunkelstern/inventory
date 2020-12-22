from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096, blank=True)

    web_link = models.URLField(null=True, blank=True)
    icon = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField('inventory.Tag', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
