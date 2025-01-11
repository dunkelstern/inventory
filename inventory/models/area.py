from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db import models
from .container import Container, CanBeContained


class Area(CanBeContained, Container):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.CharField(_("Description"), max_length=4096)
    show_sub_area = models.BooleanField(
        _("Show sub area"),
        default=True,
        help_text=_("Allow sub-areas to be defined in this area")
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    @property
    def url(self):
        return reverse("area-detail", args=[self.pk])

    class Meta:
        ordering = ("name", )
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")
