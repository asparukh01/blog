from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    image = models.ImageField(null=False, blank=False, upload_to='user_pics', verbose_name='Фото профиля')
    phone = models.CharField(max_length=12, null=False, blank=False, verbose_name="Номер телефона")
    karma = models.CharField(max_length=20, default='Не хорошая', verbose_name="Карма")
    posts_total = models.IntegerField(
        default=0,
        blank=True,
        validators=(MinValueValidator(0),)
    )
