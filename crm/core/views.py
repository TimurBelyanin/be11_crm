from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django_htmx.http import HttpResponseClientRedirect
from crm.utils.mixins import CustomHtmxMixin
from .forms import RegisterForm


class Home(LoginRequiredMixin, CustomHtmxMixin, TemplateView):
    template_name = 'partials/settings/profile.html'


class Users(LoginRequiredMixin, CustomHtmxMixin, TemplateView):
    template_name = 'partials/settings/users.html'


class NewUser(LoginRequiredMixin, CustomHtmxMixin, FormView):
    template_name = 'partials/settings/new_user.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Тут нужно будет начать процесс создания пользователя (отправка ему email для подтверждения)"""
        print("The form is absolutely correct".upper())
        return HttpResponseClientRedirect(reverse_lazy("users"))

    def form_invalid(self, form):
        print("ERRORS: ", form.errors.items())
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = error_list[0]
        print("Errors: ", errors)
        return JsonResponse({'errors': errors})
        # return HttpResponseClientRedirect(reverse_lazy("new-user"))
