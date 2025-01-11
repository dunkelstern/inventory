from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from inventory.models import Item, Settings


@method_decorator(login_required, name='dispatch')
class ItemView(DetailView):
    context_object_name = 'item'
    queryset = Item.objects.all().select_related('container', 'container__layout', 'manufacturer', 'distributor').prefetch_related('documentation')
    def get_context_data(self, *args, object_list=None, **kwargs):
        result = super().get_context_data(*args, object_list=object_list, **kwargs)
        result['settings'] = Settings.objects.first()
        return result

    def post(self, request, pk):
        item = get_object_or_404(Item.objects.filter(pk=pk))
        if request.POST.get('dec', None) is not None:
            if item.count > 0:
                item.count -= 1
                item.save()
        if request.POST.get('save', None) is not None:
            item.count = request.POST.get('amount', 0)
            item.save()
        return self.get(request)

@method_decorator(login_required, name='dispatch')
class ItemListView(ListView):
    model = Item
