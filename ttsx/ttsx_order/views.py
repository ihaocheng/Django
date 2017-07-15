#coding=utf-8

from django.shortcuts import render
from django.http import JsonResponse
from ttsx_cart.models import CartInfo
from .models import OrderDetail, OrderMain
from django.db import transaction , models
import datetime
# Create your views here.

def orderdo(request):
    uid = request.session.get('uid')
    gids = request.POST.get('gids')
    g_list = gids.split(',')
    sid = transaction.savepoint()  # 添加事物

    try:
        cart1 = CartInfo.objects.filter(goods__in=g_list, user=int(uid))

        main = OrderMain()
        time_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        uid = request.session.get('uid')
        main.orderid = '%s%d' % (time_str, uid)
        main.user_id = uid
        main.save()

        total = 0
        for cart in cart1:
            gname = cart.goods.gtitle
            if cart.count <= cart.goods.gstore:
                detail = OrderDetail()
                detail.order = main
                detail.goods = cart.goods
                detail.count = cart.count
                detail.price = cart.goods.gprice
                detail.save()
                total += detail.count * detail.price

                cart.goods.gstore -= detail.count   # 修改库存
                cart.goods.save()

                cart.delete()    # 删除购物车
            else:
                transaction.savepoint_rollback(sid) #回滚
                return JsonResponse({'result':2, 'gname':gname})   # 库存不足
        main.total = total
        main.save()
        transaction.savepoint_commit(sid)  # 提交事务

        carts = CartInfo.objects.filter(user=int(uid))
        cart_sum = carts.aggregate(models.Sum('count')).get('count__sum')
        request.session['cart_sum'] = cart_sum

        return JsonResponse({'result': 1})  # 下单成功


    except Exception as e:
        print(e)
        transaction.savepoint_rollback(sid) #回滚
        return JsonResponse({'result': 0})  # 下单失败


