from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["role", "username", "first_name", "last_name", "email", "date_of_birth", "telegram", "phone", "usdt_trc20"]