from django.contrib.auth.models import AbstractUser
from django.db import models

from dogs.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='телеграм', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

