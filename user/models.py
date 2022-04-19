from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):

    phone = models.CharField('电话号码', max_length=11, default='')
    avatar = models.CharField('头像', max_length=100, default='default.jpeg')
