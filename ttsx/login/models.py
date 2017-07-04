from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=26)
    mail = models.CharField(max_length=50, null=True, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    site = models.CharField(max_length=200, null=True, blank=True)