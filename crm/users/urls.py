from django.urls import path
from .views import LoginView, CustomLogoutView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
