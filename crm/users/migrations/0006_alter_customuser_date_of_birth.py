# Generated by Django 5.1.4 on 2025-01-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_options_alter_customuser_telegram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]
