from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Sex, Major


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'nickname', 'school', 'email', 'is_staff', 'is_active', 'is_superuser')

    def nickname(self, obj):
        return obj.profile.nickname

    def school(self, obj):
        return obj.profile.school

    nickname.short_description = '昵称'    #后台将nickname显示成“昵称”


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'sex', 'major')    #放在User中还是这里？无所谓的吧 后面加个major


@admin.register(Major)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'major')


@admin.register(Sex)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'sex')
