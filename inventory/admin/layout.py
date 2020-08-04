import json
from django.shortcuts import reverse
from django.contrib import admin
from django.conf import settings

from django.contrib.postgres.fields import JSONField
from django.forms import widgets

from inventory.models import Layout


class PrettyJSONWidget(widgets.Textarea):

    def format_value(self, value):
        try:
            value = json.dumps(json.loads(value), indent=4, sort_keys=True)
            # these lines will try to adjust size of TextArea to fit to content
            row_lengths = [len(r) for r in value.split('\n')]
            self.attrs['rows'] = min(max(len(row_lengths) + 2, 10), 30)
            self.attrs['cols'] = min(max(max(row_lengths) + 2, 40), 120)
            return value
        except Exception as e:
            logger.warning("Error while formatting JSON: {}".format(e))
            return super(PrettyJSONWidget, self).format_value(value)


class LayoutAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'changed_at']
    search_fields = ['name', 'description']
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget}
    }

    # def view_on_site(self, obj):
    #     url = reverse('layout-detail', kwargs={'id': obj.id})
    #     return settings.SERVER_URL + url

admin.site.register(Layout, LayoutAdmin)
