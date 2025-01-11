from django.utils.translation import gettext_lazy as _
from django.db import models


class FormFactor(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True, db_collation="numeric")
    description = models.CharField(_("Description"), max_length=4096, db_collation="numeric")

    icon = models.ImageField(_("Icon"), null=True, blank=True)
    datasheet = models.FileField(_("Datasheet"), null=True, blank=True)
    tags = models.ManyToManyField('inventory.Tag', verbose_name=_("Tags"), blank=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    def __str__(self):
        items = [self.name]
        items.extend([tag.description for tag in self.tags.all()])
        return ", ".join(items)

    class Meta:
        ordering = ("name", )
        verbose_name = _("Form factor")
        verbose_name_plural = _("Form factors")
