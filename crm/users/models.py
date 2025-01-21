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
        ('senior_buyer', 'Senior Buyer'),
        ('middle_buyer', 'Middle Buyer'),
        ('junior_buyer', 'Junior Buyer'),
        ('solo_buyer', 'Solo Buyer'),
        ('lead_web_developer', 'Lead Web Developer'),
        ('web_developer', 'Web Developer'),
        ('lead_designer', 'Lead Designer'),
        ('designer', 'Designer'),
        ('lead_video_creator', 'Lead Video Creator'),
        ('video_creator', 'Video Creator'),
    ]
    first_name = models.CharField(max_length=150, blank=False, verbose_name="Имя")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    telegram = models.CharField(max_length=100, unique=False, null=True, blank=True, verbose_name="Телеграм")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Номер телефона")
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name="Изображение профиля")
    usdt_trc20 = models.CharField(max_length=42, null=True, blank=True, verbose_name="Криптокошелек")

    role = models.CharField(max_length=40, choices=ROLES_CHOICES, default='solo_buyer', verbose_name="Роль")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['telegram'], condition=models.Q(telegram__isnull=False), name='unique_telegram_non_null')
        ]
