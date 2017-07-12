from django.db import models

# Create your models here.


class CartInfo(models.Model):
    goods = models.ForeignKey(to='ttsx_goods.GoodsInfo')
    user = models.ForeignKey(to='ttsx_user.UserInfo')
    count = models.IntegerField()
