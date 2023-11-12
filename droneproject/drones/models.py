from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=256)

    def __str__(self):
        return str(self.username)
