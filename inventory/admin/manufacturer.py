from django.urls import reverse
from django.contrib import admin
from django.conf import settings

from inventory.models import Manufacturer


class ManufacturerAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'changed_at']
    search_fields = ['name', 'description']
    filter_horizontal = ('tags',)

    def view_on_site(self, obj):
        url = reverse('manufacturer-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url


admin.site.register(Manufacturer, ManufacturerAdmin)
