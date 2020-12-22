from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Area

from .utils import CanBeIndexMixin


@method_decorator(login_required, name='dispatch')
class AreaView(CanBeIndexMixin, DetailView):
    context_object_name = 'area'
    queryset = Area.objects.all().select_related(
        'container',
        'layout'
    ).prefetch_related(
        'area_related',
        'box_related'
    )


@method_decorator(login_required, name='dispatch')
class AreaListView(ListView):
    model = Area
