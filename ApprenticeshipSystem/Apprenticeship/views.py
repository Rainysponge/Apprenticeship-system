from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from comment.forms import CommentForm
from user.models import Teacher, ReadNum
from comment.models import Comment
from .models import Homework


# Create your views here.
# TEST

def teacher_list(request):
    Teacher_list = Teacher.objects.all()
    users = User.objects.all()
    # profile = Profile.objects.all()
    context = {}
    context['teacher_list'] = Teacher_list
    context['users'] = users
    # context['profile'] = profile

    return render(request, 'Apprenticeship/teacher_list.html', context)


def homework_detail(request):
    homework1 = get_object_or_404(Homework, pk=1)
    # comments = Comment.objects.filter(pk=1)
    comments = Comment.objects.all()

    context = {}
    context['user'] = request.user
    context['comments'] = comments

    data = {'homework_id': homework1.id}  # 用于初始
    context['comment_form'] = CommentForm(initial=data)
    context['homework'] = homework1
    return render(request, 'Apprenticeship/homework_detail.html', context)


def teacher_info_outside(request, user_pk):
    # user_outside = User.objects.filter(pk=user_pk).first()
    # teacher = Teacher.objects.filter(pk=user_pk)    用这个获取为什么是错的？
    user = get_object_or_404(User, pk=user_pk)
    teacher = Teacher.objects.get(user=user)

    if ReadNum.objects.filter(user=user).count():
        readnum = ReadNum.objects.get(user=user)
    else:
        readnum = ReadNum(teacher=teacher, user=user)
    readnum.read_num += 1
    readnum.save()

    context = {}
    # context['user_outside'] = user_outside
    context['teacher'] = user.teacher
    return render(request, 'Apprenticeship/teacher_info_outside.html', context)


def homework_list(request):
    context = {}
    return render(request, 'Apprenticeship/homework_list.html', context)
