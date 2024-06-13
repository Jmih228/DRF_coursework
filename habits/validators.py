from rest_framework.serializers import ValidationError


class SingleCandyValidator:

    def __init__(self, reward, bounded_habit):
        self.reward = reward
        self.bounded_habit = bounded_habit

    def __call__(self, value):
        bounded_habit = dict(value).get(self.bounded_habit)
        reward = dict(value).get(self.reward)

        if bounded_habit and reward:
            raise ValidationError('Нельзя выбирать приятную привычку и награду одновременно')


class ActionTimeValidator:

    def __init__(self, execution_time):
        self.execution_time = execution_time

    def __call__(self, value):
        execution_time = dict(value).get(self.execution_time, -1)
        if execution_time < 0:
            raise ValidationError('Введите время на выполнение действия')
        if execution_time > 120:
            raise ValidationError('Нельзя задавать на выполнение привычки время более 120 секунд')


class ConsistentPracticeValidator:

    def __init__(self, rep_period):
        self.rep_period = rep_period

    def __call__(self, value):
        rep_period = dict(value).get(self.rep_period, -1)

        if rep_period < 0:
            raise ValidationError('Введите периодичность привычки')
        if rep_period > 7:
            raise ValidationError('Нельзя задавать периодичность выполнения привычки более 7 дней')


class RewardValidator:

    def __init__(self, is_nice):
        self.is_nice = is_nice

    def __call__(self, value):
        is_nice = dict(value).get(self.is_nice)

        if not is_nice:
            raise ValidationError('Привязать можно только приятную привычку')


class LimitedRewardValidator:

    def __init__(self, is_nice, reward, bounded_habit):
        self.is_nice = is_nice
        self.reward = reward
        self.bounded_habit = bounded_habit

    def __call__(self, value):
        is_nice = dict(value).get(self.is_nice)
        reward = dict(value).get(self.reward)
        bounded_habit = dict(value).get(self.bounded_habit)

        if is_nice and (reward or bounded_habit):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
