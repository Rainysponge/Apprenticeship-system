from django.contrib import admin
from django.contrib.auth.admin import User as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline, )
#
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')
