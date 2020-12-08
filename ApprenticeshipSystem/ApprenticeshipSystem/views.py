from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import Teacher, ReadNum, Profile
from Apprenticeship.models import ApprenticeRequest


def home(request):
    teachers = Teacher.objects.all().order_by('-readnum__read_num')

    read_nums = ReadNum.objects.all().order_by('-read_num')
    hot_read_nums = []
    hot_teachers = []
    # hot_users = []
    len_read_num = len(read_nums)
    if len_read_num < 3:
        for i in range(len_read_num):
            hot_read_nums.append(read_nums[i])
            hot_teachers.append(teachers[i])
    else:
        for i in range(0, 3):
            hot_read_nums.append(read_nums[i])
            hot_teachers.append(teachers[i])
            # hot_users.append(user[i])
    context = {}
    # context['require_count'] = require_count
    context['teachers'] = teachers
    context['read_nums'] = read_nums
    context['hot_read_nums'] = hot_read_nums
    context['read_numlen'] = str(len(read_nums))
    # context['users'] = users
    context['hot_teachers'] = hot_teachers
    return render(request, 'index.html', context)


def Xuanke(request):
    return render(request, 'xuanke.html', {})
