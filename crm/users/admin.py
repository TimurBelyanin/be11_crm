from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rolepermissions.admin import RolePermissionsUserAdminMixin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(RolePermissionsUserAdminMixin, admin.ModelAdmin):
    # search_fields = ()
    pass

# admin.site.register(CustomUser, CustomUserAdmin)
