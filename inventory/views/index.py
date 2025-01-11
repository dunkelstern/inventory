from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.views import redirect_to_login

from inventory.models import Settings


@method_decorator(login_required, name='post')
class IndexView(View):

    def get(self, request):
        User = get_user_model()
        if User.objects.all().count() == 0:
            # redirect to onboarding
            return redirect(reverse('onboarding'))
        if not request.user.is_authenticated:
            path = request.get_full_path()
            return redirect_to_login(path, reverse('login'))
        # check settings for correct starred index page
        settings = Settings.objects.first()
        if settings.default_container is not None:
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
