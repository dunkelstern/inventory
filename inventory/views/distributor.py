from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Distributor, Item

@method_decorator(login_required, name='dispatch')
class DistributorView(DetailView):
    context_object_name = 'distributor'
    queryset = Distributor.objects.all().prefetch_related('tags')

    def get_context_data(self, *args, object_list=None, **kwargs):
        result = super().get_context_data(*args, object_list=object_list, **kwargs)
        p = self.request.GET.get("item_page", 1)
        paginator = Paginator(Item.objects.filter(distributor=self.get_object()).select_related('container', 'manufacturer').order_by('name'), 50)
        result.update({
            "items": paginator.get_page(p)
        })
        return result

@method_decorator(login_required, name='dispatch')
class DistributorListView(ListView):
    model = Distributor
