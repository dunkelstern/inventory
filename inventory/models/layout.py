from django.utils.translation import gettext_lazy as _
from django.db import models


class Layout(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.CharField(_("Description"), max_length=4096)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)
    data = models.JSONField(_("Data"))
    template_name = models.CharField(_("Template name"), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = _("Layout")
        verbose_name_plural = _("Layouts")
