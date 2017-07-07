#coding=utf-8

from django.shortcuts import render

# Create your views here.
def index(request):
    uname = request.session.get('uname')
    context = {'title':'首页','top':'1', 'uname': uname}
    return render(request, 'goods/index.html', context)