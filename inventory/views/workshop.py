from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Workshop, Settings
from .utils import CanBeIndexMixin


@method_decorator(login_required, name='dispatch')
class WorkshopView(CanBeIndexMixin, DetailView):
    context_object_name = 'workshop'
    queryset = Workshop.objects.all().prefetch_related('area_related', 'box_related')


@method_decorator(login_required, name='dispatch')
class WorkshopListView(ListView):
    model = Workshop
