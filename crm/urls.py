from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.users.urls')),
    path('', include('crm.core.urls'))
]
