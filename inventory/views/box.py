from typing import cast, Union, List, Any
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.db.models import QuerySet

from inventory.models import Box

from .utils import CanBeIndexMixin


@method_decorator(login_required, name='dispatch')
class BoxView(CanBeIndexMixin, DetailView):
    context_object_name = 'box'
    template_name_field = 'template_name'
    queryset = Box.objects.all().select_related(
        'container',
        'layout'
    ).prefetch_related(
        'box_related'
    )

    def layout(self, obj: QuerySet, layout: list[Union[list, int]], idx=0):
        result = []
        for sublayout in layout:
            if isinstance(sublayout, list):
                resulting_sublayout, new_idx = self.layout(obj, sublayout, idx=idx)
                result.append(resulting_sublayout)
                idx = new_idx
            else:
                instances = obj.filter(index=idx).order_by('id')
                items: List[dict[str, Any]] = []

                # Add all items to the layout container
                if instances.count() > 0:
                    items.extend(list(instances))

                # Append "Add one more entry" if we do not exceed the maximum number
                # of items yet
                size = sum([item.size for item in items])
                if size < sublayout:
                    items.append({
                        "index": idx,
                        "container_id": self.object.pk
                    })

                result.append(items)
                idx += 1
        return result, idx

    def get(self, request, *args, **kwargs):
        self.object = cast(Box, self.get_object())
        context = self.get_context_data(object=self.object)
        context['layouted'], _ = self.layout(self.object.item_related.all().order_by('index'), self.object.layout.data)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class BoxListView(ListView):
    model = Box
