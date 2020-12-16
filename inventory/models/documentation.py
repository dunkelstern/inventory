from django.db import models


class Documentation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    file = models.FileField()

    def __str__(self):
        return self.file.name
