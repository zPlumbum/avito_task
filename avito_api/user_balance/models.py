from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    user_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transactions_allowed = models.BooleanField(default=True)
