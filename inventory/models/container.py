from django.db import models
from django.apps import apps


class Container(models.Model):
    layout = models.ForeignKey('inventory.Layout', on_delete=models.PROTECT, null=True, blank=True)

    def _subclass(self):
        for model in apps.get_app_config('inventory').get_models():
            if model == Container:
                continue
            if issubclass(model, Container):
                q = model.objects.filter(container_ptr_id=self.id)
                if q.exists():
                    return model, q.first()
        return Container, None

    def __str__(self):
        subclass, obj = self._subclass()
        return '{}: {}'.format(subclass.__name__, obj.name)

    @property
    def display_name(self):
        _, obj = self._subclass()
        if obj is not None:
            return obj.name
        return 'Container'


class CanBeContained(models.Model):
    container = models.ForeignKey('inventory.Container', related_name="%(class)s_related", null=True, on_delete=models.CASCADE)
    index = models.PositiveIntegerField('Index of compartment in layout')

    class Meta:
        abstract = True
