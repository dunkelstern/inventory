from django.db import models


class Distributor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    web_link = models.URLField(null=True, blank=True)
    search_link = models.URLField(help_text='Use {} for search placeholder', null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, default=None)
    icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
