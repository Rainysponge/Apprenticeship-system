from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Teacher, Student, ReadNum
from .forms import RegForm, LoginFrom, changeProfileInfoForm
from Apprenticeship.models import Homework
from comment.models import Comment
from comment.forms import CommentForm
from .tools import user_directory_path


# Create your views here.

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # school = reg_form.changed_data['school']
            user = User.objects.create_user(username, email, password)  # 创建用户
            real_name = reg_form.cleaned_data['real_name']
            sex = reg_form.cleaned_data['sex']

            nickname = reg_form.cleaned_data['nickname']
            # 这个地方就是有病
            grade = reg_form.cleaned_data['grade']
            student_ID = reg_form.cleaned_data['student_ID']
            user.save()
            profile = Profile.objects.create(user=user, sex=sex, nickname=nickname,
                                             grade=grade, student_ID=student_ID, real_name=real_name)
            profile.save()

            teacher = Teacher.objects.create(user=user, teacher_name=nickname)
            teacher.save()
            student = Student.objects.create(user=user, student_name=nickname)
            student.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'index.html', {'massage': '恭喜你已经成功注册啦，赶紧登录试试吧！'})
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    context['form_title'] = '注册'
    return render(request, 'user/register.html', context)


def login(request):
    if request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            context = {'log_massage': request.GET.get('from')}
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', context)
    else:
        login_form = LoginFrom()

    context = {}
    # context['page_title'] = '欢迎'
    context['login_form'] = login_form
    context['form_title'] = '登录'
    return render(request, 'user/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


# 这个之后要做成个人中心 要加入个人学生的信息
def teacher_info(request, teacher_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)

    context = {}
    context['teacher'] = teacher
    return render(request, 'user/teacher_info.html', context)


def changeProfileInfo(request, profile_pk):
    if request.method == 'POST':
        change_form = changeProfileInfoForm(request.POST, request.FILES)
        if change_form.is_valid():
            profile = Profile.objects.get(pk=profile_pk)
            profile.grade = change_form.cleaned_data['grade']
            profile.school = change_form.cleaned_data['school']
            profile.portrait = request.FILES['portrait']

            profile.save()

            return render(request, 'index.html', {'massage': '基础信息已经更改'})
    else:
        change_form = changeProfileInfoForm()

    context = {}
    context['change_form'] = change_form
    context['form_title'] = '更改基础信息'
    # context['ruser'] = str(request.user.username)
    return render(request, 'user/changeProfileInfo.html', context)
