from django.utils.translation import gettext_lazy as _
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.CharField(_("Description"), max_length=4096, blank=True)

    web_link = models.URLField(_("Web link"), null=True, blank=True)
    icon = models.ImageField(_("Icon"), null=True, blank=True)
    tags = models.ManyToManyField('inventory.Tag', verbose_name=_("Tags"), blank=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ("name", )
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")
