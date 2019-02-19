from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    This is an account that will be linked to a django user
    """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class SomeModel(models.Model):
    pass
