from django.contrib import admin

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
    list_display = ("owned_by", "card_type", "card_number")


class BankDetailAdmin(BaseAdmin):
    list_display = ("owned_by", "account_number", "bank")


class WebApplicationAdmin(BaseAdmin):
    list_display = ("owned_by", "url", "username", "mobile", "email")


class UPIGatewayAdmin(BaseAdmin):
    list_display = ("owned_by", "portal", "upi_id")


class SecretNoteAdmin(BaseAdmin):
    list_display = ("owned_by", "topic")


class IdentityAdmin(BaseAdmin):
    list_display = ("owned_by", "id_name", "id_number")


admin.site.register(BankCard, BankCardAdmin)
admin.site.register(BankDetail, BankDetailAdmin)
admin.site.register(WebApplication, WebApplicationAdmin)
admin.site.register(UPIGateway, UPIGatewayAdmin)
admin.site.register(SecretNote, SecretNoteAdmin)
admin.site.register(Identity, IdentityAdmin)
