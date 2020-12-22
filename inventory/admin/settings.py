from typing import Optional, TypeVar
from django.db.models import Model
from django.http.request import HttpRequest
from django.contrib import admin

from inventory.models import Settings


_ModelT = TypeVar("_ModelT", bound=Model)


class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj: Optional[_ModelT] = None) -> bool:
        return False


admin.site.register(Settings, SettingsAdmin)
