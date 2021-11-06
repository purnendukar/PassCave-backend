from django.db import models

from apps.base.models import BaseModel
from apps.user.models import User

import calendar


class AbstractCredentialModel(models.Model):
    owned_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="owned_%(class)s_cred",
        null=False,
        blank=False,
    )
    access_given = models.ManyToManyField(
        to=User,
        related_name="%(class)s_access_cred",
    )

    class Meta:
        abstract = True


class BankCard(BaseModel, AbstractCredentialModel):
    MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]
    CARD_TYPE_CHOICE = [
        ("credit_card", "Credit Card"),
        ("debit_card", "Debit Card"),
        ("atm_card", "ATM Card"),
        ("other", "Other"),
    ]
    YEAR_CHOICES = [(str(year), str(year)) for year in range(2020, 2030)]

    card_number = models.CharField(max_length=4 * 4, null=False, blank=False)
    expire_month = models.CharField(
        max_length=2, choices=MONTH_CHOICES, null=False, blank=False
    )
    expire_year = models.CharField(
        max_length=4, choices=YEAR_CHOICES, null=False, blank=False
    )
    cvv = models.CharField(max_length=3, null=False, blank=False)
    holder_name = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)
    card_type = models.CharField(
        max_length=20, choices=CARD_TYPE_CHOICE, null=False, blank=False, default=4
    )


class BankDetail(BaseModel, AbstractCredentialModel):
    account_number = models.CharField(max_length=30, null=False, blank=False)
    ifsc_code = models.CharField(max_length=20, null=False, blank=False)
    branch_code = models.CharField(max_length=20, null=False, blank=False)
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    holder_name = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)


class WebApplication(BaseModel, AbstractCredentialModel):
    url = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)


class UPIGateway(BaseModel, AbstractCredentialModel):
    upi_id = models.CharField(max_length=255, null=False, blank=False)
    portal = models.CharField(max_length=255, null=True, blank=True)
    pin = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "UPI gateway"
        verbose_name_plural = "UPI gateways"
        print(BankCard.tyu)


class SecretNote(BaseModel, AbstractCredentialModel):
    topic = models.CharField(max_length=100, null=False, blank=False)
    note = models.TextField(null=False, blank=True)


class Identity(BaseModel, AbstractCredentialModel):
    id_name = models.CharField(max_length=100, null=False, blank=False)
    id_number = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Identities"
