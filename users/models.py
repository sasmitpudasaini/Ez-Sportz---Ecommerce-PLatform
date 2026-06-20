from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # We can add phone numbers or profile pics here later
    is_customer = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)