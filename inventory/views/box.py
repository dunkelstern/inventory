from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Box


@method_decorator(login_required, name='dispatch')
class BoxView(DetailView):
    context_object_name = 'box'
    template_name_field = 'template_name'
    queryset = Box.objects.all().select_related('container', 'layout').prefetch_related('box_related').order_by('index', 'id')

    def layout(self, obj, layout, idx=0):
        result = []
        for sublayout in layout:
            if isinstance(sublayout, list):
                resulting_sublayout, new_idx = self.layout(obj, sublayout, idx=idx)
                result.append(resulting_sublayout)
                idx = new_idx
            else:
                instances = obj.filter(index=idx)
                if instances.count() == 1:
                    result.append(instances.first())
                elif instances.count() > 1:
                    sub = list(instances)
                    result.append(sub)
                else:
                    result.append({
                        "index": idx,
                        "container_id": self.object.item_related.first().container_id
                    })
                idx += 1
        return result, idx

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['layouted'], _ = self.layout(self.object.item_related.all(), self.object.layout.data)
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class BoxListView(ListView):
    model = Box
