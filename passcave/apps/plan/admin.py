from django.contrib import admin

from apps.plan.models import Plan


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "amount", "members_count")


admin.site.register(Plan, PlanAdmin)
