#coding=utf-8

from django.shortcuts import render
from django.http import JsonResponse
from models import CartInfo
from django.db.models import Sum
from ttsx.decorator import islogin

# Create your views here.

@islogin
def cart(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')
    cart = CartInfo.objects.filter(user__uname=uname)

    context = {'uname':uname, 'cart': cart, 'cart_sum':cart_sum, 'cart_tag':'0'}
    return render(request, 'cart/cart.html', context)

def add(request):
    try:
        uid = request.session.get('uid')
        uname = request.session.get('uname')
        gid = request.GET.get('gid')
        count = request.GET.get('count')
        edit = request.GET.get('edit')
        cart1 = CartInfo.objects.filter(user__uname=uname , goods=int(gid))
        if cart1 and count:
            if cart1[0].goods.gstore < cart1[0].count + int(count):
                return JsonResponse({'response':'2'})
            cart1[0].count += int(count)
            cart1[0].save()
            count = cart1[0].count
        elif edit and edit != '-1':
            cart1[0].count = int(edit)
            cart1[0].save()
            count = cart1[0].count
        elif edit == '-1':
            cart1[0].delete()
        else:
            try:
                cart = CartInfo()
                cart.user_id = int(uid)
                cart.goods_id = int(gid)
                cart.count = int(count)
                cart.save()
                count = cart.count
            except:
                count = cart1[0].count

        carts = CartInfo.objects.filter(user__uname=uname)
        cart_sum = carts.aggregate(Sum('count')).get('count__sum')
        request.session['cart_sum'] = cart_sum


        cart_sum = request.session.get('cart_sum')

        return JsonResponse({'response':'1', 'cart_sum': cart_sum, "count":count})
    except Exception as error:
        print (error)
        cart_sum = request.session.get('cart_sum')
        return JsonResponse({'response':'0', 'cart_sum':cart_sum})

@islogin
def place_order(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')

    cart_list = request.POST.getlist('cart_list')
    cart1 =CartInfo.objects.filter(id__in=cart_list)
    user = cart1[0].user

    context = {'title':'确认订单', 'uname':uname, 'cart_sum':cart_sum,
               'user':user, 'cart':cart1, 'cartids':','.join(cart_list)}
    return render(request,'cart/place_order.html',context)