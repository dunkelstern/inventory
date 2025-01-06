from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.conf import settings

from inventory.models import Tag, Item


@method_decorator(login_required, name='dispatch')
class TagView(DetailView):
    context_object_name = 'tag'
    queryset = Tag.objects.all().prefetch_related('workshop_set', 'box_set', 'distributor_set', 'manufacturer_set', 'formfactor_set')

    def get_context_data(self, *args, object_list=None, **kwargs):
        result = super().get_context_data(*args, object_list=object_list, **kwargs)
        p = self.request.GET.get("item_page", 1)
        direct_tags = Q(tags__in=[self.get_object()])
        formfactor_tags = Q(form_factor__tags__in=[self.get_object()])
        items = Item.objects.filter(direct_tags | formfactor_tags).distinct().select_related('container', 'manufacturer')
        paginator = Paginator(items, getattr(settings, "PAGE_SIZE", 10))
        result.update({
            "items": paginator.get_page(p)
        })
        return result

@method_decorator(login_required, name='dispatch')
class TagListView(ListView):
    model = Tag
