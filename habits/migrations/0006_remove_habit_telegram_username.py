# Generated by Django 5.0.6 on 2024-06-13 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_rename_telegramm_username_habit_telegram_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='telegram_username',
        ),
    ]
