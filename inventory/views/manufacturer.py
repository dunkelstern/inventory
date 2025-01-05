from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Manufacturer


class ManufacturerView(View):
    pass


@method_decorator(login_required, name='dispatch')
class ManufacturerListView(ListView):
    model = Manufacturer
