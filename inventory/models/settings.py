from django.db import models


class Settings(models.Model):
    default_container = models.ForeignKey(
        'inventory.Container',
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        help_text='Default container to display when calling the index page'
    )

    def __str__(self):
        return 'Settings'

    class Meta:
        verbose_name_plural = 'Settings'
