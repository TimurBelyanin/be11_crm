from django.urls import path
from .views import home, LoginView, logout_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="home"),
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
    path('logout/', logout_view, name='logout')

]
