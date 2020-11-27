from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse

from comment.forms import CommentForm
from comment.models import Comment
from user.models import Teacher, ReadNum
from .forms import ApprenticeForm
from .models import Homework, ApprenticeRequest


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
    context['user_out'] = user
    context['teacher'] = user.teacher
    return render(request, 'Apprenticeship/teacher_info_outside.html', context)


def homework_list(request):
    context = {}
    return render(request, 'Apprenticeship/homework_list.html', context)


def Apprentice_request(request, teacher_pk):
    teacher = Teacher.objects.get(pk=teacher_pk)
    user = request.user
    if ApprenticeRequest.objects.filter(teacher=teacher, user=user, result=0).count() == 0:
    # teacher = Teacher.objects.get(pk=teacher_pk)
    # user = request.user
        apprentice_request = ApprenticeRequest()
        apprentice_request.user = user
        apprentice_request.teacher = teacher
        apprentice_request.result = 0
        apprentice_request.save()
    else:
        pass    # 返回错误信息
    # apprentice_form = ApprenticeForm(request.POST, user=request.user)
    # data = {}
    #
    # if apprentice_form.is_valid():
    #     # 检查通过，保存数据
    #     apprentice = ApprenticeRequest()
    #     apprentice.user = apprentice_form.cleaned_data['user']
    #     apprentice.result = apprentice_form.cleaned_data['result']
    #     apprentice.teacher = 1
    #     apprentice.save()
    #
    #     # 返回数据
    #     data['status'] = 'SUCCESS'
    #     data['username'] = apprentice.user.username
    #     data['apprentice_time'] = apprentice.created_time.strftime('%Y-%m-%d %H:%M:%S')
    #     data['result'] = apprentice.result
    # else:
    #     # return render(request, 'error.html', {'message': apprentice_form.errors, 'redirect_to': referer})
    #     data['status'] = 'ERROR'
    #     data['message'] = list(apprentice_form.errors.values())[0][0]
    # return JsonResponse(data)
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)
