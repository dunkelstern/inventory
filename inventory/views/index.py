from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View

from inventory.models import Settings


@method_decorator(login_required, name='dispatch')
class IndexView(View):

    def get(self, request):
        settings = Settings.objects.first()
        if settings.default_container is not None:
            print(settings.default_container.url)
            return redirect(settings.default_container.url)
        else:
            return redirect(reverse('workshop-list'))

    def post(self, request):
        if 'index_id' in request.POST:
            settings = Settings.objects.first()
            new_container_id = int(request.POST['index_id'])
            if settings.default_container_id == new_container_id:
                settings.default_container = None
            else:
                settings.default_container_id = new_container_id
            settings.save()
            return redirect(request.META['HTTP_REFERER'])
