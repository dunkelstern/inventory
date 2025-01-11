from django.utils.translation import gettext_lazy as _

from django.urls import reverse
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.views.generic import View
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings


class OnboardingForm(forms.Form):
    username = forms.CharField(label=_("Username"), max_length=150, required=True)
    email = forms.EmailField(label=_("Email"), max_length=254, required=True)
    password = forms.CharField(label=_("Password"), max_length=1024, min_length=8, widget=forms.PasswordInput(), required=True)


class OnboardingView(View):

    def get(self, request):
        User = get_user_model()
        if User.objects.all().count() != 0:
            # redirect to index
            return redirect(reverse('index'))
        
        return TemplateResponse(request, "inventory/onboarding.html", {
            "settings": {
                "SERVER_URL": settings.SERVER_URL,
                "DEBUG": settings.DEBUG,
                "ALLOWED_HOSTS": settings.ALLOWED_HOSTS,
                "DATABASE_HOST": settings.DATABASES['default']['HOST'],
                "DATABASE_NAME": settings.DATABASES['default']['NAME'],
                "DATABASE_USER": settings.DATABASES['default']['USER'],
                "DATABASE_PASSWORD": settings.DATABASES['default']['PASSWORD'],
                "LANGUAGE_CODE": settings.LANGUAGE_CODE,
                "TIME_ZONE": settings.TIME_ZONE,
                "STATIC_ROOT": settings.STATIC_ROOT,
                "MEDIA_ROOT": settings.MEDIA_ROOT,
                "PAGE_SIZE": settings.PAGE_SIZE,
            },
            "form": OnboardingForm()
        })

    def post(self, request):
        # validate we have everything
        form = OnboardingForm(request.POST)
        if form.is_valid():
            # create superuser
            User = get_user_model()
            User.objects.create_superuser(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )

            # show success screen
            login_form = AuthenticationForm(data={"username": form.cleaned_data['username'] })
            return TemplateResponse(request, "inventory/onboarding_success.html", {"form": login_form, "next": reverse('index')})
        return TemplateResponse(request, "inventory/onboarding.html", {"settings": settings, "form": form})
