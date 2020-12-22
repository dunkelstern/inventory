from typing import Any, Dict

from inventory.models import Settings


class CanBeIndexMixin:
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['is_index'] = Settings.objects.first().default_container_id == self.object.id
        print(context)
        return context
