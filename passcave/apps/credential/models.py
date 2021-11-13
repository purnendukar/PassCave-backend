from django.db import models
from django.conf import settings

from encrypted_fields import fields

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

    _card_number = fields.EncryptedCharField(max_length=4 * 4)
    card_number = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_card_number"
    )
    expire_month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    expire_year = models.CharField(max_length=4, choices=YEAR_CHOICES)
    _cvv = fields.EncryptedCharField(max_length=3)
    cvv = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_cvv"
    )
    holder_name = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)
    card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICE, default=4)


class BankDetail(BaseModel, AbstractCredentialModel):
    _account_number = fields.EncryptedCharField(max_length=30)
    account_number = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_account_number"
    )
    _ifsc_code = fields.EncryptedCharField(max_length=20)
    ifsc_code = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_ifsc_code"
    )
    branch_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    holder_name = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)


class WebApplication(BaseModel, AbstractCredentialModel):
    url = models.CharField(max_length=255)
    _username = fields.EncryptedCharField(max_length=255, null=True, blank=True)
    username = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_username"
    )
    _mobile = fields.EncryptedCharField(max_length=15, null=True, blank=True)
    mobile = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_mobile"
    )
    _email = fields.EncryptedEmailField(null=True, blank=True)
    email = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_email"
    )
    _password = fields.EncryptedCharField(max_length=255, null=True, blank=True)
    password = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_password"
    )


class UPIGateway(BaseModel, AbstractCredentialModel):
    upi_id = models.CharField(max_length=255)
    portal = models.CharField(max_length=255, null=True, blank=True)
    _pin = fields.EncryptedCharField(max_length=8, null=True, blank=True)
    pin = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_pin"
    )

    class Meta:
        verbose_name = "UPI gateway"
        verbose_name_plural = "UPI gateways"


class SecretNote(BaseModel, AbstractCredentialModel):
    topic = models.CharField(max_length=100)
    _note = fields.EncryptedTextField(blank=True)
    note = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_note"
    )


class Identity(BaseModel, AbstractCredentialModel):
    id_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Identities"
