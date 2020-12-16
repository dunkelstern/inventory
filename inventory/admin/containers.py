from nested_admin.nested import NestedTabularInline, NestedModelAdmin, NestedStackedInline

from django.urls import reverse
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


class BoxInlineAdmin(NestedTabularInline):
    model = Box
    fk_name = 'container'
    extra = 1
    fields = ['name', 'description', 'index', 'layout']


class AreaAdmin(NestedModelAdmin):
    list_display = ['name', 'description', 'container']
    readonly_fields = ['created_at', 'changed_at']
    list_filter = ['container']
    search_fields = ['name', 'description']
    inlines = [BoxInlineAdmin]

    def view_on_site(self, obj):
        url = reverse('area-detail', kwargs={'pk': obj.id})
        return settings.SERVER_URL + url


class DocumentationInlineAdmin(NestedTabularInline):
    model = Documentation
    extra = 1


class ItemInlineAdmin(NestedStackedInline):
    model = Item
    extra = 1
    #inlines = [DocumentationInlineAdmin]


class BoxAdmin(NestedModelAdmin):
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
