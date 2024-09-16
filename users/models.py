
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту")
    phone = models.CharField(max_length=40, **NULLABLE, verbose_name="Телефон (Не обязательно)")
    country = models.CharField(max_length=50, **NULLABLE, verbose_name="Страна (Не обязательно)")
    avatar = models.ImageField(upload_to="users/avatars", **NULLABLE, verbose_name="Аватар (Не обязательно)")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
