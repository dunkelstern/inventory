import nested_admin

from django.shortcuts import reverse
from django.contrib import admin
from django.conf import settings

from inventory.models import Workshop, Area, Box, Item, Documentation


class AreaInlineAdmin(admin.TabularInline):
    model = Area
    fk_name = 'container'
    extra = 1
    fields = ['name', 'description', 'index', 'layout']


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    readonly_fields = ['created_at', 'changed_at']
    search_fields = ['name', 'description']
    inlines = [AreaInlineAdmin]

    def view_on_site(self, obj):
        url = reverse('workshop-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url

class BoxInlineAdmin(nested_admin.NestedTabularInline):
    model = Box
    fk_name = 'container'
    extra = 1
    fields = ['name', 'description', 'index', 'layout']


class AreaAdmin(nested_admin.NestedModelAdmin):
    list_display = ['name', 'description', 'container']
    readonly_fields = ['created_at', 'changed_at']
    list_filter = ['container']
    search_fields = ['name', 'description']
    inlines = [BoxInlineAdmin]

    def view_on_site(self, obj):
        url = reverse('area-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url


class DocumentationInlineAdmin(nested_admin.NestedTabularInline):
    model = Documentation
    extra = 1

class ItemInlineAdmin(nested_admin.NestedStackedInline):
    model = Item
    extra = 1
    inlines = [DocumentationInlineAdmin]

class BoxAdmin(nested_admin.NestedModelAdmin):
    list_display = ['name', 'description', 'container']
    readonly_fields = ['created_at', 'changed_at']
    list_filter = ['container']
    search_fields = ['name', 'description']
    inlines = [BoxInlineAdmin, ItemInlineAdmin]

    def view_on_site(self, obj):
        url = reverse('box-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url


admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Box, BoxAdmin)
