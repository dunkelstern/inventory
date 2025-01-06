from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.conf import settings

from inventory.models import Manufacturer, Item


@method_decorator(login_required, name='dispatch')
class ManufacturerView(DetailView):
    context_object_name = 'manufacturer'
    queryset = Manufacturer.objects.all().prefetch_related('tags')

    def get_context_data(self, *args, object_list=None, **kwargs):
        result = super().get_context_data(*args, object_list=object_list, **kwargs)
        p = self.request.GET.get("item_page", 1)
        items = Item.objects.filter(manufacturer=self.get_object()).select_related('container', 'distributor')
        paginator = Paginator(items, getattr(settings, "PAGE_SIZE", 10))
        result.update({
            "items": paginator.get_page(p)
        })
        return result


@method_decorator(login_required, name='dispatch')
class ManufacturerListView(ListView):
    model = Manufacturer
