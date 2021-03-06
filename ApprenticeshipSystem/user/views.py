from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Teacher, Student, ReadNum, Major
from .utils import get_seven_days_read_data
from .forms import RegForm, LoginFrom, changeProfileInfoForm, changePortrait, changeTeacherInfoForm, \
    changeStudentInfoForm


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
            # read_name = ReadNum.objects.create(user=user, read_num=0, teacher=teacher)

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'index.html', {'massage': '恭喜你已经成功注册啦，赶紧试试吧！'})
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
            context['massage'] = '登陆成功'
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
def teacher_info(request):
    user = request.user
    teacher = get_object_or_404(Teacher, user=user)
    dates, get_7_readNum = get_seven_days_read_data(teacher)
    context = {}
    context['teacher'] = teacher
    context['dates'] = dates
    context['get_7_readNum'] = get_7_readNum

    return render(request, 'user/teacher_info.html', context)


def changeProfileInfo(request, profile_pk):
    change_form = changeProfileInfoForm(request.POST)
    changeprotrait_form = changePortrait(request.POST, request.FILES)
    if request.method == 'POST':

        profile = Profile.objects.get(pk=profile_pk)
        if change_form.is_valid():
            # profile = Profile.objects.get(pk=profile_pk)
            profile.grade = change_form.cleaned_data['grade']
            profile.school = change_form.cleaned_data['school']
            # profile.portrait = request.FILES['portrait']
            major = change_form.cleaned_data['major']
            majorO = Major.objects.get(major=major)
            profile.major = majorO
            profile.save()
            context = {'massage': '基础信息已经更改', 'a': 1}
            return render(request, 'index.html', context)
        if changeprotrait_form.is_valid():
            profile.portrait = request.FILES['portrait']
            profile.save()
            context = {'massage': '基础信息已经更改', 'a': 1}
            return render(request, 'index.html', context)
    else:
        change_form = changeProfileInfoForm()

    context = {}
    context['change_form'] = change_form
    context['form_title'] = '更改基础信息'
    context['changeprotrait_form'] = changeprotrait_form
    # context['ruser'] = str(request.user.username)
    return render(request, 'user/changeProfileInfo.html', context)


def changeTSInfo(request, profile_pk):
    change_form = changeTeacherInfoForm(request.POST)
    # change_student_form = changeStudentInfoForm(request.POST)
    if request.method == 'POST':

        profile = Profile.objects.get(pk=profile_pk)
        teacher = Teacher.objects.get(user=profile.user)
        # student = Student.objects.get(user=profile.user)
        if change_form.is_valid():
            # profile = Profile.objects.get(pk=profile_pk)
            teacher.teacher_name = change_form.cleaned_data['teacher_name']
            teacher.skill = change_form.cleaned_data['skill']
            # profile.portrait = request.FILES['portrait']
            teacher.self_introduction = change_form.cleaned_data['self_introduction']

            teacher.save()
            context = {'massage': '老师信息已经更改'}
            return render(request, 'index.html', context)

    else:
        change_form = changeTeacherInfoForm()
        # change_student_form = changeStudentInfoForm()

    context = {}
    context['change_form'] = change_form
    context['form_title'] = '更改老师学生基本信息'
    # context['change_student_form'] = change_student_form
    # context['ruser'] = str(request.user.username)
    return render(request, 'user/changeTSInfo.html', context)


def changeTS_student_Info(request, profile_pk):
    # change_form = changeStudentInfoForm(request.POST)
    change_student_form = changeStudentInfoForm(request.POST)
    if request.method == 'POST':

        profile = Profile.objects.get(pk=profile_pk)
        # teacher = Teacher.objects.get(user=profile.user)
        student = Student.objects.get(user=profile.user)

        if change_student_form.is_valid():
            student.student_name = change_student_form.cleaned_data['student_name']
            student.help = change_student_form.cleaned_data['help']
            # profile.portrait = request.FILES['portrait']
            student.self_introduction = change_student_form.cleaned_data['self_introduction']

            student.save()
            context = {'massage': '学生信息已经更改'}
            return render(request, 'index.html', context)
    else:
        # change_form = changeTeacherInfoForm()
        change_student_form = changeStudentInfoForm()

    context = {}
    # context['change_form'] = change_form
    context['form_title'] = '更改学生基本信息'
    context['change_student_form'] = change_student_form
    # context['ruser'] = str(request.user.username)
    return render(request, 'user/changeTS_student_Info.html', context)
