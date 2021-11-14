from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from encrypted_fields import fields

import calendar

from apps.base.models import BaseModel
from apps.user.models import User


SECRET_CHOICES = (
    models.Q(app_label="secrets", model="bankcard")
    | models.Q(app_label="secrets", model="bankdetail")
    | models.Q(app_label="secrets", model="webapplication")
    | models.Q(app_label="secrets", model="upigateway")
    | models.Q(app_label="secrets", model="secretnote")
    | models.Q(app_label="secrets", model="identity")
)


class AbstractCredentialModel(models.Model):
    owned_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="owned_%(class)s_cred",
    )
    access_given = models.ManyToManyField(to=User, related_name="%(class)s_access_cred")

    class Meta:
        abstract = True


class Secret(BaseModel):
    title = models.CharField(max_length=255)
    # Below the mandatory fields for generic relation
    secret_type = models.ForeignKey(
        ContentType, limit_choices_to=SECRET_CHOICES, on_delete=models.CASCADE
    )
    secret_id = models.UUIDField()
    secret_object = GenericForeignKey(ct_field="secret_type", fk_field="secret_id")

    class Meta:
        unique_together = ("secret_type", "secret_id")
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title


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
    secret = GenericRelation(
        Secret,
        object_id_field="secret_id",
        content_type_field="secret_type",
        limit_choices_to=SECRET_CHOICES,
        related_query_name="bank_cards",
    )


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
    secret = GenericRelation(
        Secret,
        object_id_field="secret_id",
        content_type_field="secret_type",
        limit_choices_to=SECRET_CHOICES,
        related_query_name="bank_details",
    )


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
    secret = GenericRelation(
        Secret,
        object_id_field="secret_id",
        content_type_field="secret_type",
        limit_choices_to=SECRET_CHOICES,
        related_query_name="web_apps",
    )


class UPIGateway(BaseModel, AbstractCredentialModel):
    _upi_id = fields.EncryptedCharField(max_length=255)
    upi_id = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_upi_id"
    )
    portal = models.CharField(max_length=255, null=True, blank=True)
    _pin = fields.EncryptedCharField(max_length=8, null=True, blank=True)
    pin = fields.SearchField(
        hash_key=settings.SEARCH_HASH_KEY, encrypted_field_name="_pin"
    )
    secret = GenericRelation(
        Secret,
        object_id_field="secret_id",
        content_type_field="secret_type",
        limit_choices_to=SECRET_CHOICES,
        related_query_name="upi_gateways",
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
    secret = GenericRelation(
        Secret,
        object_id_field="secret_id",
        content_type_field="secret_type",
        limit_choices_to=SECRET_CHOICES,
        related_query_name="secret_notes",
    )


class Identity(BaseModel, AbstractCredentialModel):
    id_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    secret = GenericRelation(
        Secret,
        object_id_field="secret_id",
        content_type_field="secret_type",
        limit_choices_to=SECRET_CHOICES,
        related_query_name="identities",
    )

    class Meta:
        verbose_name_plural = "Identities"
