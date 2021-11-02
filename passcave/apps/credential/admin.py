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


admin.site.register(BankCard, BaseAdmin)
admin.site.register(BankDetail, BaseAdmin)
admin.site.register(WebApplication, BaseAdmin)
admin.site.register(UPIGateway, BaseAdmin)
admin.site.register(SecretNote, BaseAdmin)
admin.site.register(Identity, BaseAdmin)
