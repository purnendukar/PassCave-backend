from django.contrib import admin

from apps.secret_group.models import SecretGroup


# Register your models here.
class SecretGroupAdmin(admin.ModelAdmin):
    list_display = ("admin", "grp_type")


admin.site.register(SecretGroup, SecretGroupAdmin)
