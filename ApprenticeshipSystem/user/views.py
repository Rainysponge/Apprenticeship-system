from django.shortcuts import render
from .forms import RegForm, LoginFrom
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile


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

