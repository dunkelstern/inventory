from django.db import models


class Layout(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    data = models.JSONField()
    template_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
