from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомный пользователь."""

    foot_length = models.PositiveSmallIntegerField(
        verbose_name='Размер ноги',
        blank=True,
        null=True,
    )
