#coding=utf-8
from django.shortcuts import render, redirect
from models import UserInfo
from hashlib import sha1
# Create your views here.

def register(request):
    context = {'title':'注册'}
    return render(request, 'user/register.html',context)

def register_check(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    email = post.get('email')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    u = UserInfo()
    u.uname = uname
    u.upwd = upwd_sha1
    u.umail = email
    u.save()
    return redirect('/user/login/')


def login(request):
    context = {'title':'登陆'}
    return render(request, 'user/login.html')

def login_check(request):
    post = request.POST()
    uname = post.get('uname')
    upwd = post.get('upwd')

    ulist = UserInfo.objects.filter(uname=uname)
    if ulist:
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        if ulist[0].upwd == upwd_sha1:
            pass #登陆，保存状态COOKIE
        else:
            pass #密码错误，重新登陆 
    else:
        pass #没有此用户
