from django.urls import reverse
from django.contrib import admin
from django.conf import settings

from inventory.models import Distributor


class DistributorAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'changed_at']
    search_fields = ['name', 'description']

    def view_on_site(self, obj):
        url = reverse('distributor-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url


admin.site.register(Distributor, DistributorAdmin)
