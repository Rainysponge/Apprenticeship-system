#23课28：56
#23课8:20 HTTP_REFERER获取当前页面信息 reverse解析urls中home的路径，这里使用为啥是跳到当前页面？
from django import forms
from django.shortcuts import render, redirect
from .models import Comment
from Apprenticeship.models import Homework
from django.urls import reverse
from comment.forms import CommentForm
# Create your views here.


def update_comment(request):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = request.user
        # comment.text = text
        # comment.content_object = Homework.objects.get(pk=object_id)
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = Homework.objects.get(pk=comment_form.cleaned_data['homework_id'])
        comment.save()

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)

