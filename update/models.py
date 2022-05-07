from django.db import models


class Newslist(models.Model):

    title = models.CharField('title', max_length=15)
    href = models.CharField('href', max_length=100)
    info = models.CharField('info', max_length=100)

