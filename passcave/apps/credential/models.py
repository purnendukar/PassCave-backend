from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from utils.base.models import BaseModel
from apps.user.models import User

import calendar
from datetime import date

# Create your models here.

class BankCard(BaseModel):
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]
    CARD_TYPE_CHOICE = [
        (1, "Credit Card"),
        (2, "Debit Card"),
        (3, "ATM Card"),
        (4, "Other")
    ]
    YEAR_CHOICES = [(i,year) for i,year in enumerate(range(2020, 2030))]

    card_number = models.CharField(
        max_length= 4*4,
        null=False,
        blank=False
    )
    expire_month = models.CharField(
        max_length=20,
        choices=MONTH_CHOICES,
        null=False,
        blank=False
    )
    expire_year = models.CharField(
        max_length=12,
        choices=YEAR_CHOICES,
        null=False,
        blank=False
    )
    cvv = models.CharField(
        max_length=3,
        null=False,
        blank=False
    )
    holder_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    bank = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    card_type = models.CharField(
        max_length=20,
        choices=CARD_TYPE_CHOICE,
        null=False,
        blank=False,
        default=4
    )


class BankDetail(BaseModel):
    account_number = models.CharField(
        max_length= 30,
        null=False,
        blank=False
    )
    ifsc_code = models.CharField(
        max_length= 20,
        null=False,
        blank=False
    )
    branch_code = models.CharField(
        max_length= 20,
        null=False,
        blank=False
    )
    branch_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    holder_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    bank = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


class WebApplication(BaseModel):
    url = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    username = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    mobile = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    password = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )


class UPIGateway(BaseModel):
    upi_id = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    portal = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    pin = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )


class SecretNote(BaseModel):
    topic = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    note = models.TextField(
        null=False,
        blank=True
    )


class Identity(BaseModel):
    id_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    id_number = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    image = models.ImageField(
        null=True,
        blank=True
    )


class Credential(BaseModel):
    CRED_TYPES = models.Q(app_label='credential', model='BankCard') | \
            models.Q(app_label='credential', model='BankDetail') | \
            models.Q(app_label='credential', model='UPIGateway') | \
            models.Q(app_label='credential', model='WebApplication') | \
            models.Q(app_label='credential', model='SecretNote') | \
            models.Q(app_label='credential', model='Identity')
                
    cred_type = models.ForeignKey(
        ContentType, 
        limit_choices_to=CRED_TYPES,
        on_delete=models.CASCADE,
        null=True,
    )
    owned_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    owned_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="credential_owned",
        null=False,
        blank=False
    )
    access_given = models.ManyToManyField(
        to=User,
        related_name="credential_access"
    )
    object_id = models.UUIDField(
        null=False,
        blank=False
    )
    detail = GenericForeignKey(
        'cred_type',
        'object_id'
    )
