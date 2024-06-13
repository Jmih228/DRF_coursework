from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Аватар')
    tg_chat_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='Чат id пользователя в телеграмме')
    telegram_username = models.CharField(max_length=200, verbose_name='Имя пользователя в телеграмме')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
