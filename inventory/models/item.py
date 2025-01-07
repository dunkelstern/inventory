from django.utils.translation import gettext_lazy as _
from django.db import models

from .container import CanBeContained


class Item(CanBeContained):
    name = models.TextField(_("Name"), max_length=255, db_collation="numeric")
    description = models.CharField(_("Description"), max_length=4096, db_collation="numeric")
    size = models.PositiveIntegerField(
        _("Size"),
        default=1,
        help_text=_("Number of sub-compartments this item takes up")
    )
    form_factor = models.ForeignKey(
        'inventory.FormFactor', 
        verbose_name=_("Form factor"), 
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    manufacturer = models.ForeignKey(
        'inventory.Manufacturer',
        verbose_name=_("Manufacturer"),
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    distributor = models.ForeignKey(
        'inventory.Distributor',
        verbose_name=_("Distributor"),
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    distributor_item_no = models.CharField(
        _("Distributor item no."),
        max_length=255,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        _("Price"),
        decimal_places=3,
        max_digits=7,
        null=True,
        blank=True
    )
    last_ordered_on = models.DateField(_("Last ordered on"), null=True, blank=True)
    documentation = models.ManyToManyField(
        'inventory.Documentation',
        verbose_name=_("Documentation"),
        related_name='items',
        blank=True
    )
    tags = models.ManyToManyField(
        'inventory.Tag',
         verbose_name=_("Tags"),
         blank=True
    )

    count = models.PositiveIntegerField(
        _("Count"),
        default=1,
        null=False,
        help_text=_("Number of parts available")
    )
    low_count = models.PositiveIntegerField(
        _("Low watermark"),
        default=0,
        null=False,
        help_text=_("Low watermark on which to alert ordering more")
    )

    metadata = models.JSONField(_("Custom metadata, used by templates"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    changed_at = models.DateTimeField(_("Changed at"), auto_now=True)

    def __str__(self):
        items = [self.name, self.description]
        items.extend([tag.description for tag in self.tags.all()])
        items.append(str(self.form_factor))
        return ", ".join(items)

    @property
    def all_tags(self):
        if self.form_factor:
            return list(self.tags.all()) + list(self.form_factor.tags.all())
        else:
            return list(self.tags.all())
    
    @property
    def value(self):
        return self.count * self.price

    class Meta:
        ordering = ("name", )
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
