from django.db import models


class Settings(models.Model):
    default_container = models.ForeignKey(
        'inventory.Container',
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
    )
    track_amount = models.BooleanField(
        default=False,
        help_text="Show item count in overview and warn on low watermarks"
    )
    currency = models.CharField(max_length=30, help_text="Currency name", default="Euro")
    currency_symbol = models.CharField(max_length=20, default="&euro;")
    currency_symbol_position = models.BooleanField(
        default=True,
        help_text="Currency symbol after amount"
    )

    def __str__(self):
        return 'Settings'

    class Meta:
        verbose_name_plural = 'Settings'
