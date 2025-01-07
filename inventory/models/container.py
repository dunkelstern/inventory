from django.utils.translation import gettext_lazy as _
from django.db import models
from django.apps import apps


class Container(models.Model):
    layout = models.ForeignKey(
        'inventory.Layout',
        verbose_name=_("Layout"),
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    @property
    def subclass(self):
        for model in apps.get_app_config('inventory').get_models():
            if model == Container:
                continue
            if issubclass(model, Container):
                q = model.objects.filter(container_ptr_id=self.pk)
                if q.exists():
                    return model, q.first()
        return Container, None

    def __str__(self):
        subclass, obj = self.subclass
        return '{}: {}'.format(subclass.__name__, obj.name)

    @property
    def display_name(self):
        _, obj = self.subclass
        if obj is not None:
            return obj.name
        return _("Container")

    @property
    def url(self):
        _, obj = self.subclass
        if obj is not None:
            return obj.url
        return None

    class Meta:
        verbose_name = _("Container")
        verbose_name_plural = _("Containers")

class CanBeContained(models.Model):
    container = models.ForeignKey(
        'inventory.Container',
        verbose_name=_("Container"),
        related_name="%(class)s_related",
        null=True,
        on_delete=models.CASCADE
    )
    index = models.PositiveIntegerField(_("Index of compartment in layout"))

    class Meta:
        abstract = True

    @property
    def container_url(self):
        _, obj = self.container.subclass
        return obj.url
