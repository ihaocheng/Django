#coding=utf-8

from django.shortcuts import render
from django.core.paginator import Paginator
from models import TypeInfo, GoodsInfo

# Create your views here.
def index(request):
    uname = request.session.get('uname')
    tlist = TypeInfo.objects.all() #类型对象

    alist = []
    for i in tlist:
        goods_list = i.goodsinfo_set.order_by('-id')[:4]
        click_list = i.goodsinfo_set.order_by('-gclick')[:3]
        alist.append({'type':i, 'goods':goods_list, 'click':click_list})

    context = {'uname':uname, 'top':'1', 'title':'首页', 'alist':alist}
    return render(request, 'goods/index.html', context)

def goods_list(request, tid, pid):
    uname = request.session.get('uname')
    context = {'uname':uname, 'top':'1'}
    if not tid:
        goods_list = GoodsInfo.objects.all()
    else:
        t = TypeInfo.objects.get(pk=int(tid))
        goods_list = t.goodsinfo_set.order_by('-id')
        context['t'] = t

    new_goods = goods_list[:2]
    context['new_goods'] = new_goods

    paginator = Paginator(goods_list, 14)
    goods_page = paginator.page(1)
    context['goods'] = goods_page

    return render(request, 'goods/list.html', context)