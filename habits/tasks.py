from celery import shared_task
from django.conf import settings
from datetime import datetime, timedelta
from habits.models import Habit
from pytz import timezone as tz
import requests
from users.models import CustomUser


@shared_task
def habit_reminder_func():

    token = settings.TG_BOT_TOKEN
    url = f"https://api.telegram.org/bot{token}/"
    habits = Habit.objects.all()
    now = datetime.now()
    warning_time = (now + timedelta(minutes=10)).time().replace(tzinfo=tz('UTC'))
    tg_username = ''
    data = requests.get(url + "getupdates").json()

    for habit in habits:
        habit_time = habit.time.replace(tzinfo=tz('UTC'))
        user = CustomUser.objects.get(pk=habit.user.id)

        if warning_time > habit_time and now.time().replace(tzinfo=tz('UTC')) < habit_time:
            if data.get('result'):
                tg_username = data['result'][0]['message']['chat']['username']

            if tg_username == user.telegram_username and user.tg_chat_id is None:
                user.tg_chat_id = data['result'][0]['message']['chat']['id']

            message_text = f'В {habit.time}  вы должны {habit.action} в {habit.place}'

            requests.get(url + f'sendMessage?chat_id={user.tg_chat_id}&text={message_text}')
