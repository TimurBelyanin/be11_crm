

    # def clean_role(self):
    #     role = self.cleaned_data['role']
    #     valid_roles = dict(CustomUser.ROLES_CHOICES)
    #     if role not in valid_roles.values():
    #         raise forms.ValidationError(f"Invalid role. Choose one from the list.")
    #     return role

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ["role", "username", "first_name", "last_name", "email", "date_of_birth", "telegram", "phone", "usdt_trc20"]
#
#     def clean_role(self):
#         role = self.cleaned_data.get('role')
#
#         valid_roles = dict(CustomUser.ROLES_CHOICES)
#         if role not in valid_roles:
#             raise forms.ValidationError(f"Invalid role. Choose one from the list.")
#
#         return role
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#
#         if CustomUser.objects.filter(username=username).exists():
#             raise ValidationError("A user with this username already exists.")
#
#         if not username.isalpha():
#             raise forms.ValidationError("Username must contain only letters (A-Z).")
#
#         # Проверка на длину
#         if len(username) < 3 or len(username) > 15:
#             raise forms.ValidationError("Username must be between 3 and 15 characters.")
#
#         return username
#
#     def clean_first_name(self):
#         first_name = self.cleaned_data.get('first_name')
#
#         if not first_name.isalpha():
#             raise forms.ValidationError("First name must contain only letters.")
#
#         if len(first_name) < 2 or len(first_name) > 20:
#             raise forms.ValidationError("First name must be between 2 and 20 characters.")
#
#         return first_name
#
#     def clean_last_name(self):
#         last_name = self.cleaned_data.get('last_name')
#
#         # Проверка на латиницу или кириллицу
#         if not last_name.isalpha():
#             raise forms.ValidationError("Last name must contain only letters.")
#
#         # Проверка на длину
#         if len(last_name) < 2 or len(last_name) > 20:
#             raise forms.ValidationError("Last name must be between 2 and 20 characters.")
#
#         return last_name
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#
#         if CustomUser.objects.filter(email=email).exists():
#             raise ValidationError("A user with this email already exists.")
#
#         validator = EmailValidator()
#         try:
#             validator(email)
#         except ValidationError:
#             raise forms.ValidationError("Enter a valid email address.")
#
#         return email
#
#     def clean_telegram(self):
#         telegram = self.cleaned_data.get('telegram')
#         print("Telegram from clean_telegram: ", telegram)
#         print("Cleaned data from CLean_Telegram method: ", self.cleaned_data)
#
#         if CustomUser.objects.filter(telegram=telegram).exists():
#             raise ValidationError("A user with this telegram already exists.")
#         # Проверка на латиницу и цифры
#         if telegram and not telegram.isalnum():
#             raise forms.ValidationError("Telegram username must contain only letters and numbers.")
#
#         return telegram
#
#     def clean_phone(self):
#         phone = self.cleaned_data.get('phone')
#
#         # Проверка: мобильный телефон (пример для формата +7XXXXXXXXXX, можно адаптировать под нужный формат)
#         if phone and not re.match(r'^\+?[1-9]\d{1,14}$', phone):
#             raise forms.ValidationError("Phone number must be valid and in the correct format (e.g. +7XXXXXXXXXX).")
#         return phone
#
#     def clean_usdt_trc20(self):
#         usdt_trc20 = self.cleaned_data.get('usdt_trc20')
#
#         # Проверка: кошелек, только латиница и цифры, строго 34 символа
#         if len(usdt_trc20) != 34 or not re.match(r'^[a-zA-Z0-9]{34}$', usdt_trc20):
#             raise forms.ValidationError(
#                 "USDT TRC20 address must be exactly 34 characters long and contain only Latin letters and digits.")
#         return usdt_trc20
#
