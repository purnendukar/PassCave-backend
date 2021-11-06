from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.plan.models import Plan
from apps.base.models import BaseModel
from apps.user.managers import UserManager

# Create your models here.


class User(BaseModel, AbstractUser):
    objects = UserManager()
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
    email = models.EmailField(unique=True, db_index=True)
    secret_key = models.CharField(max_length=255, blank=True)


class UserProfile(BaseModel):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, related_name="profile"
    )
    plan = models.OneToOneField(
        to=Plan, on_delete=models.CASCADE, null=False, blank=False
    )
