from django.db import models


class Documentation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    file = models.FileField()
    item = models.ForeignKey('inventory.Item', on_delete=models.CASCADE, related_name='documentation')
