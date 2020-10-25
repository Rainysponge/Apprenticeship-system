from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginFrom, RegForm


def home(request):
    return render(request, 'index.html', {})

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
    context['login_form'] = login_form
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
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
    return render(request, 'register.html', context)
