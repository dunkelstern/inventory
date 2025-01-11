from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.template.loader import get_template, TemplateDoesNotExist
from django.db import models
from .container import CanBeContained, Container


class Box(CanBeContained, Container):
    name = models.CharField(_("Name"), max_length=255, unique=True)
    description = models.CharField(_("Description"), max_length=4096)
    tags = models.ManyToManyField('inventory.Tag', verbose_name=_("Tags"), blank=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    @property
    def template_name(self):
        if self.layout.template_name:
            template = 'inventory/box-' + self.layout.template_name + '.html'
        else:
            template = 'inventory/box-' + slugify(self.layout.name) + '.html'
        try:
            get_template(template)
            return template
        except TemplateDoesNotExist:
            return 'inventory/box-generic.html'

    @property
    def url(self):
        return reverse("box-detail", args=[self.pk])

    class Meta:
        ordering = ("name", )
        verbose_name = _("Box")
        verbose_name_plural = _("Boxes")
