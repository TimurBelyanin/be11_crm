from django import forms
from crm.users.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator, MinLengthValidator, MaxLengthValidator
import re


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field_name = field_name.replace("_", " ")
            error_messages = {
                'invalid_choice': f'Incorrect {field_name} format',
                'required': f'Incorrect {field_name} format',
                'max_length': f'Incorrect {field_name} format',
                'min_length': f'Incorrect {field_name} format',
                'invalid': f'Incorrect {field_name} format'
            }
            field.error_messages = error_messages

    class Meta:
        model = CustomUser
        fields = ["role", "username", "first_name", "last_name", "email", "date_of_birth", "telegram", "phone", "usdt_trc20"]

    role = forms.ChoiceField(choices=CustomUser.ROLES_CHOICES, required=True)

    username = forms.CharField(
        validators=[
            RegexValidator(r'^[a-zA-Z]{3,15}$'),
            MinLengthValidator(3),
            MaxLengthValidator(15)
        ],
        required=True
    )

    first_name = forms.CharField(
        validators=[
            RegexValidator(r'^[a-zA-Zа-яА-Я]{2,20}$'),
            MinLengthValidator(2),
            MaxLengthValidator(20)
        ],
        required=True
    )

    last_name = forms.CharField(
        validators=[
            RegexValidator(r'^[a-zA-Zа-яА-Я]{2,20}$'),
            MinLengthValidator(2),
            MaxLengthValidator(20)
        ],
        required=False
    )

    email = forms.EmailField(validators=[EmailValidator()], required=False)

    date_of_birth = forms.DateField(required=False)

    telegram = forms.CharField(
        validators=[
            RegexValidator(r'^@[a-zA-Z0-9]+$'),
        ],
        required=False
    )

    phone = forms.CharField(
        validators=[RegexValidator(r'^\+7\d{10}$')],
        required=False
    )

    usdt_trc20 = forms.CharField(
        validators=[RegexValidator(r'^[a-zA-Z0-9]{34}$')],
        required=False
    )

    def clean_telegram(self):
        telegram = self.cleaned_data.get('telegram')
        if telegram == '':
            return None
        return telegram

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        telegram = cleaned_data.get("telegram")

        if username and CustomUser.objects.filter(username=username).exists():
            print("КАКОГО ХЕРА БЛЯТЬ")
            raise forms.ValidationError({"username": "A user with this username already exists."})

        if email and CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError({"email": "A user with this email already exists."})

        if telegram and CustomUser.objects.filter(telegram=telegram).exists():
            raise forms.ValidationError({"telegram": "A user with this telegram already exists."})

        return cleaned_data
