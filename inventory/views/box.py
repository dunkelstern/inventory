from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Box


@method_decorator(login_required, name='dispatch')
class BoxView(DetailView):
    context_object_name = 'box'
    queryset = Box.objects.all().select_related('container', 'layout').prefetch_related('box_related')


@method_decorator(login_required, name='dispatch')
class BoxListView(ListView):
    model = Box

