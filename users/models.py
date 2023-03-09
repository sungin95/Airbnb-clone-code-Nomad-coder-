from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(
        default=False
    )  # True or False 둘만 있을 수 있는데 방법은 둘 default=False 혹은 null=True(없어도 된다.)
