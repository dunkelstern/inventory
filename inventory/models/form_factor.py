from django.db import models


class FormFactor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)

    icon = models.ImageField(null=True, blank=True)
    datasheet = models.FileField(null=True, blank=True)
    tags = models.ManyToManyField('inventory.Tag', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        items = [self.name]
        items.extend([tag.description for tag in self.tags.all()])
        return ", ".join(items)

    class Meta:
        ordering = ("name", )
