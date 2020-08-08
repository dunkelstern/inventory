from django.utils.text import slugify
from django.template.loader import get_template, TemplateDoesNotExist
from django.db import models
from .container import CanBeContained, Container


class Box(CanBeContained, Container):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Boxes'

    @property
    def template_name(self):
        template = 'inventory/box-' + slugify(self.layout.name) + '.html'
        try:
            get_template(template)
            return template
        except TemplateDoesNotExist:
            return 'inventory/box-generic.html'
