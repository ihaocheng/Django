#coding=utf8
from django.db import models

# Create your models here.

class OrderMain(models.Model):
    orderid=models.CharField(max_length=20,primary_key=True)#20170713000000用户id
    order_time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey('ttsx_user.UserInfo')
    total=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    state=models.IntegerField(default=0)

class OrderDetail(models.Model):
    order=models.ForeignKey(OrderMain)
    goods=models.ForeignKey('ttsx_goods.GoodsInfo')
    count=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
