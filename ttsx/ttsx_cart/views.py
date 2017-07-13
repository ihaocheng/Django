#coding=utf-8

from django.shortcuts import render
from django.http import JsonResponse
from models import CartInfo
from django.db.models import Sum
from ttsx.decorator import islogin

# Create your views here.

@islogin
def index(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')
    print(cart_sum)
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
        print(gid, edit, count)
        cart1 = CartInfo.objects.filter(user__uname=uname , goods=int(gid))
        print (cart1)
        if cart1 and count:
            cart1[0].count += int(count)
            cart1[0].save()
            count = cart1[0].count
        elif edit:
            cart1[0].count = int(edit)
            cart1[0].save()
            count = cart1[0].count
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
                print(count)

        carts = CartInfo.objects.filter(user__uname=uname)
        cart_sum = carts.aggregate(Sum('count')).get('count__sum')
        request.session['cart_sum'] = cart_sum


        cart_sum = request.session.get('cart_sum')

        return JsonResponse({'response':'1', 'cart_sum': cart_sum, "count":count})
    except Exception as error:
        print (error)
        cart_sum = request.session.get('cart_sum')
        return JsonResponse({'response':'0', 'cart_sum':cart_sum})