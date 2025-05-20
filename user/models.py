from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone_number = models.CharField(max_length=35, verbose_name="Номер телефона", blank=True, null=True, help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to="user/avatar/", blank=True, null=True, help_text="Ваше фото")
    country = models.CharField(max_length=15, verbose_name="Страна", blank=True, null=True, help_text="Ваша страна")

    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email