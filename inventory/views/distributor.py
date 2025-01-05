from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from inventory.models import Distributor


class DistributorView(View):
    pass


@method_decorator(login_required, name='dispatch')
class DistributorListView(ListView):
    model = Distributor
