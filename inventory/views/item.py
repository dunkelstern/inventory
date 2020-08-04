from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Item


@method_decorator(login_required, name='dispatch')
class ItemView(DetailView):
    context_object_name = 'item'
    queryset = Item.objects.all().select_related('container', 'container__layout', 'manufacturer', 'distributor').prefetch_related('documentation')


@method_decorator(login_required, name='dispatch')
class ItemListView(ListView):
    model = Item
