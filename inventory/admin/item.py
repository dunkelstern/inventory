from django.shortcuts import reverse
from django.contrib import admin
from django.conf import settings

from inventory.models import Item, Documentation


class DocumentationInlineAdmin(admin.TabularInline):
    model = Documentation
    extra = 1


class ItemAdmin(admin.ModelAdmin):
    list_display = ['container', 'index', 'name', 'description']
    list_display_links = ['name', 'description']
    list_filter = ['container']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'changed_at']
    inlines = [DocumentationInlineAdmin]

    def view_on_site(self, obj):
        url = reverse('item-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url

admin.site.register(Item, ItemAdmin)
