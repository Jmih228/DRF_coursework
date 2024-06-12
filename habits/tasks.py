from celery import shared_task
from django.conf import settings
from datetime import datetime, timedelta
from habits.models import Habit
from pytz import timezone as tz
import requests


@shared_task
def habit_reminder_func():

    token = settings.TG_BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/"
    habits = Habit.objects.all()
    now = datetime.now()
    warning_time = (now + timedelta(minutes=10)).time().replace(tzinfo=tz('UTC'))

    for habit in habits:
        habit_time = habit.time.replace(tzinfo=tz('UTC'))

        if warning_time > habit_time and now.time().replace(tzinfo=tz('UTC')) < habit_time:
            data = requests.get(url + "getupdates").json()
            chat_id = data['result'][0]['message']['chat']['id']

            requests.get(url + f'sendMessage?chat_id={chat_id}&text=В {habit.time}  вы должны {habit.action} в {habit.place}')
