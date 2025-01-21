from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView
from django_htmx.http import HttpResponseClientRedirect
from crm.utils.mixins import CustomHtmxMixin
from .forms import RegisterForm
from rolepermissions.roles import assign_role

from ..users.models import CustomUser


class Home(LoginRequiredMixin, CustomHtmxMixin, TemplateView):
    template_name = 'partials/settings/profile.html'


class Users(LoginRequiredMixin, CustomHtmxMixin, TemplateView):
    template_name = 'partials/settings/users.html'

    def get_context_data(self, **kwargs):
        users = CustomUser.objects.all()
        context = super().get_context_data(**kwargs)
        context['users'] = users
        return context


class NewUser(LoginRequiredMixin, CustomHtmxMixin, FormView):
    template_name = 'partials/settings/new_user.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users')

    def form_valid(self, form):
        """Тут нужно будет начать процесс создания пользователя"""
        user = form.save()
        role = form.cleaned_data.get("role")
        assign_role(user, role)

        if self.request.htmx:
            return HttpResponseClientRedirect(self.success_url)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("ERRORS: ", form.errors.items())
        errors = {}
        for field, error_list in form.errors.items():
            errors[field] = error_list[0]
        print("Errors: ", errors)
        return JsonResponse({'errors': errors})
        # return HttpResponseClientRedirect(reverse_lazy("new-user"))
