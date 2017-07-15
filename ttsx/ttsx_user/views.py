#coding=utf-8
from django.shortcuts import render, redirect
from models import UserInfo
from ttsx_goods.models import GoodsInfo
from hashlib import sha1
from django.http import JsonResponse, HttpResponse
from ttsx_cart.models import CartInfo
from django.db.models import Sum
from ttsx_order.models import OrderDetail

# Create your views here.
from ttsx import decorator
def register(request):
    context = {'title':'注册', 'top' : '0'}
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
    if not request.session.get('uname'):
        context = {'title':'登陆', 'top' : '0'}
        uname = request.COOKIES.get('uname')
        if uname:
            context['uname'] = uname
        return render(request, 'user/login.html',context)
    else:
        return redirect('/')

def login_check(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')
    ulist = UserInfo.objects.filter(uname=uname)

    if ulist: #二次判断，防止js被禁用
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        if ulist[0].upwd == upwd_sha1:
            uid = ulist[0].id
            request.session['uname'] = uname
            request.session['uid'] = uid
            cart_sum = CartInfo.objects.filter(user=int(uid)).aggregate(Sum('count'))
            request.session['cart_sum'] = cart_sum['count__sum']
            url = request.session.get('url_path','/')
            response =  redirect(url)
            if post.get('checkbox') == 'on':
                response.set_cookie('uname',uname,3600*2)
            return response
        else:
            return redirect('/user/login/')
    else:
        return redirect('/user/login/')

def login_check2(request): #ajax判断
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('upwd')

    ulist = UserInfo.objects.filter(uname=uname)

    if ulist:
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()

        if ulist[0].upwd == upwd_sha1:
            return JsonResponse({'check': '2'})
        else:
            return JsonResponse({'check':'1'}) #密码错误

    else:
        return JsonResponse({'check':'0'}) #用户名不存在

def logout(request):
    url = request.session.get('url_path','/')
    request.session.flush()
    request.session['url_path'] = url
    return redirect(url)

@decorator.islogin
def center_info(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')

    context = {'title': '用户中心', 'uname':uname , 'cart_sum':cart_sum}
    if uname:
        user = UserInfo.objects.filter(uname=uname)
        context['user'] = user[0]

    gid_str = request.COOKIES.get('glance','')
    gid_list = gid_str.split(',')
    gid_list = gid_list[1:][::-1]
    goods = []
    for gid in gid_list:
        goods.append(GoodsInfo.objects.filter(pk=int(gid))[0])
    context['goods'] = goods

    return render(request, 'user/user_center_info.html', context)

@decorator.islogin
def center_order(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')




    context = {'title':'订单', 'uname':uname, 'cart_sum':cart_sum}
    return render(request, 'user/user_center_order.html', context)

@decorator.islogin
def center_site(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')

    user = UserInfo.objects.filter(uname=uname)[0]

    context = {'title': '收货地址', 'uname':uname, 'user':user, 'cart_sum':cart_sum}
    return render(request, 'user/user_center_site.html', context)

def site_set(request):
    uname = request.session.get('uname')
    user = UserInfo.objects.filter(uname=uname)[0]

    post = request.POST
    rname = post.get('rname')
    uaddress = post.get('uaddress')
    rcode = post.get('ucode')
    utel = post.get('utel')

    user.rname = rname
    user.uaddress = uaddress
    user.rcode = rcode
    user.utel = utel
    user.save()
    return redirect('/user/center_site/')