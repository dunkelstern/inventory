from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from .container import Container


class Workshop(Container):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.CharField(_("Description"), max_length=4096)
    show_boxes = models.BooleanField(
        _("Show boxes"),
        default=True,
        help_text=_("Allow boxes to be defined directly in this workshop")
    )
    tags = models.ManyToManyField('inventory.Tag', verbose_name=_("Tags"), blank=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    @property
    def url(self):
        return reverse("workshop-detail", args=[self.pk])

    class Meta:
        ordering = ("name", )
        verbose_name = _("Workshop")
        verbose_name_plural = _("Workshops")
