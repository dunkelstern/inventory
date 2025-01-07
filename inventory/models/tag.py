from django.utils.translation import gettext_lazy as _
from django.db import models


class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True, db_collation="numeric")
    description = models.CharField(_("Description"), max_length=4096, db_collation="numeric")
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'pk']
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
