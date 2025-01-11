from django.utils.translation import gettext_lazy as _
from django.db import models


class Documentation(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    file = models.FileField()

    def __str__(self):
        return self.file.name

    class Meta:
        ordering = ("name", )
        verbose_name = _("Documentation")
        verbose_name_plural = _("Documentation")
