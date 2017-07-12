#coding=utf-8

from django.shortcuts import render
from django.http import JsonResponse
from models import CartInfo

# Create your views here.

def index(request):
    uname = request.session.get('uname')
    context = {'uname':uname, }
    return render(request, 'cart/cart.html', context)

def add(request):
    try:
        count = request.GET.get('count')
        gid = request.GET.get('gid')


        return JsonResponse({'response':'1'})
    except:
        return JsonResponse({'response':'0'})