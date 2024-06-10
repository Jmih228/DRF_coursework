from django.urls import path
from habits.views import (PublicHabitsListAPIView,
                          UserHabitsListAPIView,
                          HabitCreateAPIView,
                          HabitRetrieveAPIView,
                          HabitUpdateAPIView,
                          HabitDestroyAPIView)
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('public_habits/', PublicHabitsListAPIView.as_view(), name='public_habits'),
    path('my_habits/', UserHabitsListAPIView.as_view(), name='my_habits'),
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('my_habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_view'),
    path('habit_update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit_delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete')
]
