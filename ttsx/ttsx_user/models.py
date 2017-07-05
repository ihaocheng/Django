from django.db import models
from datetime import datetime
# Create your models here.

class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)#sha1
    umail=models.CharField(max_length=30)
    uaddress=models.CharField(default='',max_length=100)
    utel=models.CharField(default='',max_length=11)

    rname=models.CharField(default='',max_length=20)
    rcode=models.CharField(default='',max_length=6)
    updata = models.DateField(default=datetime.now())
