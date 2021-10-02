from django.contrib import admin
from apps.credential.models import (
    Credential
)

# Register your models here.
class CredentialAdmin(admin.ModelAdmin):
    pass

admin.site.register(Credential, CredentialAdmin)