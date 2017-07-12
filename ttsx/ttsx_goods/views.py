#coding=utf-8

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from models import TypeInfo, GoodsInfo

# Create your views here.
def index(request):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')
    tlist = TypeInfo.objects.all() #类型对象

    alist = []
    for i in tlist:
        goods_list = i.goodsinfo_set.order_by('-id')[:4]
        click_list = i.goodsinfo_set.order_by('-gclick')[:3]
        alist.append({'type':i, 'goods':goods_list, 'click':click_list})

    context = {'uname':uname, 'title':'首页', 'alist':alist , 'cart_sum':cart_sum}
    return render(request, 'goods/index.html', context)

def goods_list(request, tid, pindex):
    if not pindex:  # 分页索引值，默认为1
        pindex = 1
    uname = request.session.get('uname') # 模板中js代码判断登陆状态
    cart_sum = request.session.get('cart_sum')
    context = {'uname':uname, 'title':'商品列表' , 'cart_sum':cart_sum}

    # tag = request.session.get('tag') # 使用session传参
    # tag = request.GET.get('tag') # 使用地址栏参数传参
    tag = request.COOKIES.get('tag')
    print(tag)
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
    if tid == '0' or (not tid):
        goods_list = GoodsInfo.objects.all().order_by(ord_str)
        goods_list2 = GoodsInfo.objects.all().order_by('-id')
        t = {'id':'0'}
        context['t'] = t
    else:
        t = TypeInfo.objects.get(pk=int(tid))
        goods_list = t.goodsinfo_set.order_by(ord_str)
        goods_list2 = t.goodsinfo_set.order_by('-id')
        context['t'] = t

    new_goods = goods_list2[:2]
    context['new_goods'] = new_goods

    paginator = Paginator(goods_list, 5)
    psum = paginator.num_pages

    pindex = int(pindex)
    # left = (pindex // 5) * 5 + 1
    # right = (pindex // 5 + 1) * 5 + 1
    left = pindex - 2
    right = pindex + 3
    # if pindex%5 == 0:
    #     left-=5
    #     right-=5
    if right > psum:
        right = psum+1
    if left < 1:
        left = 1
        right = 6

    page_range = range(left, right)

    goods_page = paginator.page(int(pindex))
    context['goods'] = goods_page
    context['cla'] = cla
    context['page_range'] = page_range
    return render(request, 'goods/list.html', context)

# def list_tag(request):
#     tag = request.GET.get('tag')
#     request.session['tag'] = tag
#     return JsonResponse({}) #ajax 必须返回一个jsonresponse ，服务器才执行写入session

def detail(request, tid, gid):
    uname = request.session.get('uname')
    cart_sum = request.session.get('cart_sum')

    if tid == '0':
        new_goods = GoodsInfo.objects.all().order_by('-id')[:2]
    else:
        t = TypeInfo.objects.get(pk=int(tid))
        new_goods = t.goodsinfo_set.order_by('-id')[:2]
    goods = GoodsInfo.objects.filter(pk=int(gid))[0]

    goods.gclick += 1 # 点击量加1
    goods.save()

    context = {'uname':uname, 'title':'商品详细信息',
               'new_goods':new_goods, 'goods':goods, 'cart_sum':cart_sum}

    gid_str = request.COOKIES.get('glance','')
    gid_list = gid_str.split(',')
    print(gid_list)
    if str(goods.id) in gid_list: # 删除旧的浏览记录
        gid_list.remove(str(goods.id))
        print("删除")
        print(gid_list)
    gid_str = ",".join(gid_list)
    gid_str += ",%s" % goods.id

    response =  render(request, 'goods/detail.html', context)
    response.set_cookie('glance', gid_str)

    return response

def query(request):
    return render(request,'goods/query.html')

def search(request, page):
    if not page:
        page = 1
    page = int(page)

    query = request.GET.get('q')
    paginator = Paginator(query, 10)
    page = paginator.page(page)
    return render(request, 'search/search.html',
                  {'page': page, 'title':'搜索结果','uname':'laoma'})

