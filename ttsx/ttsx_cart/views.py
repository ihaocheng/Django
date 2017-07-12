#coding=utf-8

from django.shortcuts import render
from django.http import JsonResponse
from models import CartInfo
from django.db.models import Sum

# Create your views here.

def index(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')
    print(cart_sum)
    cart = CartInfo.objects.filter(user__uname=uname)

    context = {'uname':uname, 'cart': cart, 'cart_sum':cart_sum}
    return render(request, 'cart/cart.html', context)

def add(request):
    try:
        uid = request.session.get('uid')
        uname = request.session.get('uname')
        gid = request.GET.get('gid')
        count = request.GET.get('count')

        cart = CartInfo.objects.filter(user__uname=uname , goods=int(gid))
        print (cart)
        if cart:
            cart[0].count += int(count)
            cart[0].save()
        else:
            cart = CartInfo()
            cart.user_id = int(uid)
            cart.goods_id = int(gid)
            cart.count = int(count)
            cart.save()

        carts = CartInfo.objects.filter(user__uname=uname)
        cart_sum = carts.aggregate(Sum('count')).get('count__sum')
        request.session['cart_sum'] = cart_sum


        cart_sum = request.session.get('cart_sum')

        return JsonResponse({'response':'1', 'cart_sum': cart_sum})
    except Exception as error:
        print (error)
        cart_sum = request.session.get('cart_sum')
        return JsonResponse({'response':'0', 'cart_sum':cart_sum})