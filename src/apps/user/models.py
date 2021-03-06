# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    subscriptions = models.ManyToManyField(
        'self', symmetrical=False, related_name='subscribers'
    )
