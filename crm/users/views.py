from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.shortcuts import render
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_active:
            return redirect('home')
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(f"USER: {user}")

        if user is not None:
            login(request, user)
            home_url = reverse('home')
            return render(request, 'partials/confirmed.html', {'home_url': home_url})
            # return HttpResponseClientRedirect(home_url)
        else:
            try:
                user = get_user_model().objects.get(username=username)
                if user.is_active:
                    return render(request, 'partials/password-incorrect.html')
                else:
                    return render(request, 'partials/frozen.html')
            except get_user_model().DoesNotExist:
                return render(request, 'partials/password-incorrect.html')


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        return HttpResponseClientRefresh()