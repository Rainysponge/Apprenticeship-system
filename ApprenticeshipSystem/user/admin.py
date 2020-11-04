from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Sex, Major, Student, Teacher


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

    nickname.short_description = '昵称'  # 后台将nickname显示成“昵称”


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'sex', 'major')


@admin.register(Student)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'enter_time', 'grade', 'help', 'self_introduction')


@admin.register(Teacher)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'enter_time', 'grade', 'skill', 'self_introduction')


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('id', 'major')


@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('id', 'sex')
