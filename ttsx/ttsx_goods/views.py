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

def goods_list(request, tid, pindex):
    if not pindex:  # 分页索引值，默认为1
        pindex = 1
    url = request.path # 取得不带参数的路径
    uname = request.session.get('uname') # js判断登陆状态
    context = {'uname':uname, 'top':'1', 'url':url}

    tag = request.session.get('tag')

    print ("list: %s" % tag)
    if tag == 'price':
        ord_str = 'gprice'
    elif tag == 'click':
        ord_str = '-gclick'
    else:
        ord_str = '-id'

    # 无tid为全部分类
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

    paginator = Paginator(goods_list, 15)
    goods_page = paginator.page(int(pindex))
    context['goods'] = goods_page
    return render(request, 'goods/list.html', context)

def tag(request):
    tag = request.GET.get('tag')
    print("tag: " % tag)

    request.session['tag'] = tag


