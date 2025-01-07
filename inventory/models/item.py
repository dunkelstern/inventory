from django.db import models

from .container import CanBeContained


class Item(CanBeContained):
    name = models.TextField(max_length=255, db_collation="numeric")
    description = models.CharField(max_length=4096, db_collation="numeric")
    size = models.PositiveIntegerField(default=1, help_text="Number of sub-compartments this item takes up")
    form_factor = models.ForeignKey('inventory.FormFactor', null=True, blank=True, on_delete=models.PROTECT)
    manufacturer = models.ForeignKey('inventory.Manufacturer', null=True, blank=True, on_delete=models.PROTECT)
    distributor = models.ForeignKey('inventory.Distributor', null=True, blank=True, on_delete=models.PROTECT)
    distributor_item_no = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(decimal_places=3, max_digits=7, null=True, blank=True)
    last_ordered_on = models.DateField(null=True, blank=True)
    documentation = models.ManyToManyField('inventory.Documentation', related_name='items', blank=True)
    tags = models.ManyToManyField('inventory.Tag', blank=True)

    count = models.PositiveIntegerField(
        default=1,
        null=False,
        help_text="Number of parts available"
    )
    low_count = models.PositiveIntegerField(
        default=0,
        null=False,
        help_text="Low watermark on which to alert ordering more"
    )


    def __str__(self):
        items = [self.name, self.description]
        items.extend([tag.description for tag in self.tags.all()])
        items.append(str(self.form_factor))
        return ", ".join(items)

    @property
    def all_tags(self):
        if self.form_factor:
            return list(self.tags.all()) + list(self.form_factor.tags.all())
        else:
            return list(self.tags.all())
    
    @property
    def value(self):
        return self.count * self.price

    class Meta:
        ordering = ("name", )
