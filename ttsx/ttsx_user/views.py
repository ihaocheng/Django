#coding=utf-8
from django.shortcuts import render, redirect
from models import UserInfo
from hashlib import sha1
from django.http import JsonResponse
# Create your views here.

def register(request):
    context = {'title':'注册'}
    return render(request, 'user/register.html',context)

def register_check2(request):
    uname = request.GET.get('uname')
    uname = UserInfo.objects.filter(uname=uname)
    if not uname:
        check = '0'
    else:
        check = '1'
    return JsonResponse({'check':check})

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
    #if request.method == 'GET'

    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    print(uname)
    print(upwd)

    ulist = UserInfo.objects.filter(uname=uname)
    print(ulist)
    if ulist:
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        if ulist[0].upwd == upwd_sha1:
            request.session['uname'] = uname
            return redirect('/user/user_center_info/')
        else:
            return JsonResponse({'check':'1'})

    else:
        return JsonResponse({'check':'0'})

def user_center_info(request):
    return render(request, 'user/user_center_info.html')