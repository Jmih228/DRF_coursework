from django.db import models
from django.conf import settings


class Habit(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name='Пользователь')
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(verbose_name='Время',
                            help_text='Вверите время на выполнение привычки в секундах')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_nice = models.BooleanField(verbose_name='Признак приятной привычки')
    bounded_habit = models.ForeignKey('Habit', on_delete=models.DO_NOTHING,
                                      null=True, blank=True, verbose_name='Связанная привычка')
    reward = models.CharField(max_length=255, null=True, blank=True, verbose_name='Награда')
    rep_period = models.SmallIntegerField(default=1, verbose_name='Периодичнось',
                                          help_text='Введите частоту выполнения привычки в днях')
    execution_time = models.SmallIntegerField(default=120, verbose_name='Время на выполнение')
    is_public = models.BooleanField(verbose_name='Признак публичности')

    class Meta:

        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'

    def __str__(self):
        return self.action
