from django.contrib import admin
from .models import *


# Register your models here.

# @admin.register(Student)
# class BlogTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'enter_time', 'grade', 'help', 'self_introduction')
#
#
# @admin.register(Teacher)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'enter_time', 'grade', 'skill', 'self_introduction')


@admin.register(Relationship)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'SID', 'TID', 'created_time')


@admin.register(Homework)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'relationship_id', 'content')


@admin.register(Critic)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'homework_id', 'content')


@admin.register(ApprenticeRequest)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'teacher', 'created_time', 'result')
