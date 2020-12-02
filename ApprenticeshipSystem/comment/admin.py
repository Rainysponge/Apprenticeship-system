from django.contrib import admin
from .models import Comment, Teacher_Comment
# Register your models here.


@admin.register(Comment)
class CommentDetailAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'text', 'comment_time', 'user')


@admin.register(Teacher_Comment)
class CommentDetailAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'text', 'comment_time', 'user')
