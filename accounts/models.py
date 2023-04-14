from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser에 birthday 속성이 포함되지 않아 models에 별도로 추가
class User(AbstractUser):
    birthday = models.DateField(null = True, blank=True)
    image = models.ImageField(null = True, blank=True)