# homework_pk报错 还有homework.html找不到url 'update_comment'
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Teacher, Student
from .forms import RegForm, LoginFrom
from Apprenticeship.models import Homework
from comment.models import Comment


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

            sex = reg_form.cleaned_data['sex']
            user.save()
            nickname = reg_form.cleaned_data['nickname']
            # 这个地方就是有病
            grade = reg_form.cleaned_data['grade']
            profile = Profile.objects.create(user=user, sex=sex, nickname=nickname, grade=grade)
            profile.save()

            teacher = Teacher.objects.create(user=user, teacher_name=nickname)
            teacher.save()
            student = Student.objects.create(user=user, student_name=nickname)
            student.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return render(request, 'index.html', {'massge': '恭喜你已经成功注册啦，赶紧登录试试吧！'})
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
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', {})
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


# def homework(request, homework_pk):
def homework(request):
    homework1 = get_object_or_404(Homework, pk=1)
    # comments = Comment.objects.filter(pk=1)
    comments = Comment.objects.all()

    context = {}
    context['user'] = request.user
    context['comments'] = comments
    context['homework'] = homework1
    return render(request, 'user/homework.html', context)


def teacher_list(request):
    # tlist = Teacher.objects.get()

    context = {}
    # context['teacher_list'] = tlist

    return render(request, 'user/teacher_list.html', context)


def teacher_info(request, teacher_pk):
    teacher = get_object_or_404(Teacher, pk=teacher_pk)

    context = {}
    context['teacher'] = teacher
    return render(request, 'user/teacher_info.html', context)
