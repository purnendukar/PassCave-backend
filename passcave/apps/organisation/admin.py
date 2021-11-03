from django.contrib import admin

from apps.organisation.models import Organisation


# Register your models here.
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("admin", "org_type")


admin.site.register(Organisation, OrganisationAdmin)
