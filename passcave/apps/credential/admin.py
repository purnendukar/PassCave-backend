from django.contrib import admin
from encrypted_fields import fields

from apps.credential.models import (
    BankCard,
    BankDetail,
    WebApplication,
    UPIGateway,
    SecretNote,
    Identity,
)


class BaseAdmin(admin.ModelAdmin):
    filter_horizontal = ("access_given",)


class BankCardAdmin(BaseAdmin):
    list_display = (
        "owned_by",
        "holder_name",
        "card_type",
        "card_number",
        "expire_month",
        "expire_year",
    )
    list_filter = ("card_type", "expire_month", "expire_year")
    search_fields = ("owned_by", "bank", "card_number", "holder_name")
    fields = (
        "owned_by",
        "access_given",
        "bank",
        "holder_name",
        "card_type",
        "card_number",
        "cvv",
        "expire_month",
        "expire_year",
    )


class BankDetailAdmin(BaseAdmin):
    list_display = ("owned_by", "account_number", "bank")
    fields = (
        "owned_by",
        "access_given",
        "account_number",
        "holder_name",
        "bank",
        "branch_code",
        "branch_name",
    )
    search_fields = ("owned_by", "account_number", "bank")


class WebApplicationAdmin(BaseAdmin):
    list_display = ("owned_by", "url", "username", "mobile", "email")
    fields = (
        "owned_by",
        "access_given",
        "url",
        "username",
        "mobile",
        "email",
        "password",
    )
    search_fields = ("owned_by", "url", "username", "mobile", "email")


class UPIGatewayAdmin(BaseAdmin):
    list_display = ("owned_by", "portal", "upi_id")
    fields = ("owned_by", "access_given", "portal", "upi_id", "pin")
    search_fields = ("owned_by", "portal", "upi_id")


class SecretNoteAdmin(BaseAdmin):
    list_display = ("owned_by", "topic")
    fields = ("owned_by", "topic", "note")
    search_fields = ("owned_by", "topic")


class IdentityAdmin(BaseAdmin):
    list_display = ("owned_by", "id_name", "id_number")
    search_fields = ("owned_by", "id_name", "id_number")


admin.site.register(BankCard, BankCardAdmin)
admin.site.register(BankDetail, BankDetailAdmin)
admin.site.register(WebApplication, WebApplicationAdmin)
admin.site.register(UPIGateway, UPIGatewayAdmin)
admin.site.register(SecretNote, SecretNoteAdmin)
admin.site.register(Identity, IdentityAdmin)
