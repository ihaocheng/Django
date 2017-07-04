#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from models import UserInfo
# Create your views here.

def login(request):
    return render(request, 'login.html')

def login_check(request):
    uname = request.POST.get('username')
    passwd = request.POST.get('pwd')
    urow = UserInfo.objects.get(uname)
    if urow:
        if urow.password == passwd:
            return HttpResponse('ok')
        else:
            return HttpResponse('password error')
    else:
        return HttpResponse('请注册')


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')