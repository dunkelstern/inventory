from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from django.db import models


class Settings(models.Model):
    default_container = models.ForeignKey(
        'inventory.Container',
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        help_text=_("Default container to display when calling the index page")
    )
    track_amount = models.BooleanField(
        default=False,
        help_text=_("Show item count in overview and warn on low watermarks")
    )
    currency = models.CharField(_("Currency"), max_length=30, help_text=_("Currency name"), default="Euro")
    currency_symbol = models.CharField(_("Currency symbol"), max_length=20, default="&euro;")
    currency_symbol_position = models.BooleanField(
        _("Currency symbol at end"),
        default=True,
        help_text=_("Currency symbol after amount")
    )

    def __str__(self):
        return gettext("Settings")

    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settings")
