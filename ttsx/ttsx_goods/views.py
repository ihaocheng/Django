#coding=utf-8

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
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

def goods_list(request, tid, pindex):
    if not pindex:  # 分页索引值，默认为1
        pindex = 1
    uname = request.session.get('uname') # 模板中js代码判断登陆状态
    context = {'uname':uname, 'top':'1', 'title':'商品列表'}

    # tag = request.session.get('tag') # 使用session传参
    tag = request.GET.get('tag') # 使用地址栏参数传参
    if tag == 'price':
        ord_str = 'gprice'
        cla = {'price':'active', 'click':'', 'default':''}
    elif tag == 'click':
        ord_str = '-gclick'
        cla = {'price':'', 'click':'active', 'default':''}

    else:
        ord_str = '-id'
        cla = {'price': '', 'click': '', 'default': 'active'}

    # 无tid默认为全部分类
    if not tid:
        goods_list = GoodsInfo.objects.all().order_by(ord_str)
        goods_list2 = GoodsInfo.objects.all().order_by('-id')
    else:
        t = TypeInfo.objects.get(pk=int(tid))
        goods_list = t.goodsinfo_set.order_by(ord_str)
        goods_list2 = t.goodsinfo_set.order_by('-id')
        context['t'] = t

    new_goods = goods_list2[:2]
    context['new_goods'] = new_goods

    paginator = Paginator(goods_list, 5)
    goods_page = paginator.page(int(pindex))
    context['goods'] = goods_page
    context['cla'] = cla
    return render(request, 'goods/list.html', context)

def list_tag(request):
    tag = request.GET.get('tag')
    request.session['tag'] = tag
    return JsonResponse({}) #ajax 必须返回一个jsonresponse ，服务器才执行写入session



