from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

from .container import CanBeContained


class Item(CanBeContained):
    name = models.TextField(max_length=255)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    metadata = models.JSONField('Custom metadata, used by templates', blank=True, null=True)
    form_factor = models.ForeignKey('inventory.FormFactor', null=True, blank=True, on_delete=models.PROTECT)

    manufacturer = models.ForeignKey('inventory.Manufacturer', null=True, blank=True, on_delete=models.PROTECT)
    distributor = models.ForeignKey('inventory.Distributor', null=True, blank=True, on_delete=models.PROTECT)
    distributor_item_no = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(decimal_places=3, max_digits=7, null=True, blank=True)
    last_ordered_on = models.DateField(null=True, blank=True)
    documentation = models.ManyToManyField('inventory.Documentation', related_name='items', blank=True)
    tags = models.ManyToManyField('inventory.Tag', blank=True)

    def __str__(self):
        return self.name