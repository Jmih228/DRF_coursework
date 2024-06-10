from rest_framework import serializers
from habits.models import Habit
from habits.validators import (SingleCandyValidator,
                               ActionTimeValidator,
                               ConsistentPracticeValidator,
                               RewardValidator,
                               LimitedRewardValidator,)


class HabitSerializer(serializers.ModelSerializer):

    Validators = [SingleCandyValidator(reward='reward', bounded_habit='bounded_habit'),
                  ActionTimeValidator(execution_time='execution_time'),
                  ConsistentPracticeValidator(rep_period='rep_period'),
                  RewardValidator(is_nice='is_nice'),
                  LimitedRewardValidator(is_nice='is_nice', reward='reward',
                                         bounded_habit='bounded_habit')]

    class Meta:
        model = Habit
        fields = '__all__'
