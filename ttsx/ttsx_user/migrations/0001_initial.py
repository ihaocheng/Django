# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('umail', models.CharField(max_length=30)),
                ('uaddress', models.CharField(default=b'', max_length=100)),
                ('utel', models.CharField(default=b'', max_length=11)),
                ('rname', models.CharField(default=b'', max_length=20)),
                ('rcode', models.CharField(default=b'', max_length=6)),
                ('updata', models.DateField(default=datetime.datetime(2017, 7, 5, 16, 40, 32, 229279))),
            ],
        ),
    ]
