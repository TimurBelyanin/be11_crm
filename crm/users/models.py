# from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLES_CHOICES = [
        ('owner', 'Owner'),
        ('admin', 'Admin'),
        ('head_of_buying', 'Head Of Buying'),
        ('senior_team_lead', 'Senior Team Lead'),
        ('middle_team_lead', 'Middle Team Lead'),
        ('junior_team_lead', 'Junior Team Lead'),
        ('solo_buyer', 'Solo Buyer'),
        ('senior_buyer', 'Senior Buyer'),
        ('middle_buyer', 'Middle Buyer'),
        ('junior_buyer', 'Junior Buyer'),
    ]

    date_of_birth = models.DateField(verbose_name="Дата рождения")
    telegram = models.CharField(max_length=100, null=True, blank=True, verbose_name="Телеграм")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Номер телефона")
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name="Изображение профиля")
    usdt_trc20 = models.CharField(max_length=42, null=True, blank=True, verbose_name="Криптокошелек")

    role = models.CharField(max_length=40, choices=ROLES_CHOICES, default='solo_buyer', verbose_name="Роль")
