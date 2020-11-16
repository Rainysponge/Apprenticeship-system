from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginFrom, RegForm
from user.models import Teacher, ReadNum, Profile


def home(request):
    teachers = Teacher.objects.all().order_by('-readnum__read_num')
    # hot_teachers = []
    # for i in range(0, 3):
    #     hot_teachers.append(teachers[i])
    # users = User.objects.all().order_by('-')

    read_nums = ReadNum.objects.all().order_by('-read_num')
    hot_read_nums = []
    hot_teachers = []
    # hot_users = []

    for i in range(0, 3):
        hot_read_nums.append(read_nums[i])
        hot_teachers.append(teachers[i])
        # hot_users.append(user[i])
    context = {}
    context['teachers'] = teachers
    context['read_nums'] = read_nums
    context['hot_read_nums'] = hot_read_nums
    # context['users'] = users
    context['hot_teachers'] = hot_teachers
    return render(request, 'index.html', context)


def Xuanke(request):
    return render(request, 'xuanke.html', {})
