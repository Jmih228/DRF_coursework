from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'place', 'time', 'is_nice', 'bounded_habit', 'reward',
                    'rep_period', 'execution_time', 'is_public')
    list_filter = ('id', 'user', 'place', 'is_nice', 'bounded_habit',
                   'reward', 'rep_period', 'execution_time', 'is_public')
    search_fields = ('id', 'user', 'action', 'place', 'time', 'bounded_habit',
                     'reward', 'execution_time',)
