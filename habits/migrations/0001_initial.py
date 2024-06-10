# Generated by Django 5.0.6 on 2024-06-10 04:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NiceHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место')),
                ('time', models.SmallIntegerField(default=120, help_text='Вверите время на выполнение привычки в секундах', verbose_name='Время')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('rep_period', models.SmallIntegerField(default=1, help_text='Введите частоту выполнения привычки в днях', verbose_name='Периодичнось')),
                ('execution_time', models.TimeField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(verbose_name='Признак публичности')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Приятная ривычка',
                'verbose_name_plural': 'Приятные привычки',
            },
        ),
        migrations.CreateModel(
            name='UsefulHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место')),
                ('time', models.SmallIntegerField(default=120, help_text='Вверите время на выполнение привычки в секундах', verbose_name='Время')),
                ('action', models.CharField(max_length=150, verbose_name='Действие')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='Награда')),
                ('rep_period', models.SmallIntegerField(default=1, help_text='Введите частоту выполнения привычки в днях', verbose_name='Периодичнось')),
                ('execution_time', models.TimeField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(verbose_name='Признак публичности')),
                ('bounded_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='habits.nicehabit', verbose_name='Вознаграждение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Полезная привычка',
                'verbose_name_plural': 'Полезные привычки',
            },
        ),
    ]