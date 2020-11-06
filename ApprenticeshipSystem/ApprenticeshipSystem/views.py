from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginFrom, RegForm


def home(request):
    return render(request, 'index.html', {})


def Xuanke(request):
    return render(request, 'xuanke.html', {})

