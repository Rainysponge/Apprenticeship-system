#homework_pk报错 还有homework.html找不到url 'update_comment'
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
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
            user.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            # return redirect(request.GET.get('from', reverse('home')))
            return render(request, 'index.html', {})
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


# 这里想实现一个首页浮窗登录
# def loginTohome(request):
#     if request.method == 'POST':
#         login_form = LoginFrom(request.POST)
#         if login_form.is_valid():
#             user = login_form.cleaned_data['user']
#             auth.login(request, user)
#             # return redirect(request.GET.get('from', reverse('home')))
#             return render(request, 'index.html', {})
#     else:
#         login_form = LoginFrom()
#
#     context = {}
#     # context['page_title'] = '欢迎'
#     context['login_form'] = login_form
#     context['form_title'] = '登录'
#     return render(request, 'index.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


#def homework(request, homework_pk):
def homework(request):
    homework = get_object_or_404(Homework, pk=1)
    #comments = Comment.objects.filter(pk=1)
    comments = Comment.objects.all()

    context = {}
    context['user'] = request.user
    context['comments'] = comments
    context['homework'] = homework
    return render(request, 'user/homework.html', context)
