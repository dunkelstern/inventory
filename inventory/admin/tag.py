from django.contrib import admin

from inventory.models import Tag


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'changed_at']
    search_fields = ['name', 'description']
    list_display = ['name', 'description']


admin.site.register(Tag, TagAdmin)
