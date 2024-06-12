from rest_framework.test import (APITestCase,
                                 APIClient)
from rest_framework import status
from habits.models import Habit
from users.models import CustomUser


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='user@sky.pro', password='hghghg777')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.private_habit = Habit.objects.create(
            user=self.user,
            place='test_place',
            time='7:30:00',
            action='test_action',
            is_nice=True,
            reward='test_reward',
            rep_period=1,
            execution_time=120,
            is_public=False,
            telegram_username='qwe'
        )

    def test_public_habits(self):
        Habit.objects.create(
            user=self.user,
            place='test_place',
            time='7:30:00',
            action='test_action',
            is_nice=True,
            reward='test_reward',
            rep_period=1,
            execution_time=120,
            is_public=True,
            telegram_username='qwe'
        )

        response = self.client.get(
            '/public_habits/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()[0],
            {'id': 8, 'place': 'test_place', 'time': '07:30:00', 'action': 'test_action', 'is_nice': True,
             'reward': 'test_reward', 'rep_period': 1, 'execution_time': 120, 'is_public': True,
             'telegram_username': 'qwe', 'user': 6, 'bounded_habit': None}
        )

    def test_my_habits(self):
        response = self.client.get(
            '/my_habits/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'][0],
            {'id': 6, 'place': 'test_place', 'time': '07:30:00', 'action': 'test_action', 'is_nice': True,
             'reward': 'test_reward', 'rep_period': 1, 'execution_time': 120, 'is_public': False,
             'telegram_username': 'qwe', 'user': 5, 'bounded_habit': None}
        )

    def test_habit_create(self):
        data = {
            'user': self.user.id,
            'place': 'test_place',
            'time': '7:30:00',
            'action': 'test_action',
            'is_nice': True,
            'reward': 'test_reward',
            'rep_period': 1,
            'execution_time': 120,
            'is_public': True,
            'telegram_username': 'qwe'
        }

        response = self.client.post(
            '/habit_create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'place': 'test_place', 'time': '07:30:00', 'action': 'test_action', 'is_nice': True,
             'reward': 'test_reward', 'rep_period': 1, 'execution_time': 120, 'is_public': True,
             'telegram_username': 'qwe', 'user': 1, 'bounded_habit': None}
        )

    def test_habit_retrieve_view(self):
        response = self.client.get(
            f'/my_habits/{self.private_habit.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 4, 'place': 'test_place', 'time': '07:30:00', 'action': 'test_action', 'is_nice': True,
             'reward': 'test_reward', 'rep_period': 1, 'execution_time': 120, 'is_public': False,
             'telegram_username': 'qwe', 'user': 3, 'bounded_habit': None}
        )

    def test_habit_update(self):
        data = {
            'place': 'update',
            'action': 'update'
        }

        response = self.client.patch(
            f'/habit_update/{self.private_habit.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 5, 'place': 'update', 'time': '07:30:00', 'action': 'update', 'is_nice': True,
             'reward': 'test_reward', 'rep_period': 1, 'execution_time': 120, 'is_public': False,
             'telegram_username': 'qwe', 'user': 4, 'bounded_habit': None}
        )

    def test_habit_delete(self):
        response = self.client.delete(
            f'/habit_delete/{self.private_habit.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
