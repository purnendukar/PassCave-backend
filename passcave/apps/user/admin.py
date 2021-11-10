from django.contrib import admin

from apps.user.models import User, UserProfile


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "employee"


class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)


admin.site.register(User, UserAdmin)
