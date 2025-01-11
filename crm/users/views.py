from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.shortcuts import render
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            home_url = reverse('home')
            # return JsonResponse({'redirect': home_url})
            return HttpResponseClientRedirect(home_url)
        else:
            return render(request, 'partials/button-error.html')


@login_required
def home(request):
    if request.htmx:
        return render(request, 'partials/test.html')
    print(request.htmx)
    # return render(request, 'common/base_dashboard.html')
    return render(request, 'common/base_dashboard.html')


def logout_view(request):
    logout(request)
    return HttpResponseClientRefresh()
