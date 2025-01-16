from django.urls import path
from .views import Home, Users, NewUser
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('users/', Users.as_view(), name="users"),
    path('create-new-user/', NewUser.as_view(), name="new-user")
]
