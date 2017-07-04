# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=26)),
                ('mail', models.CharField(max_length=50, null=True, blank=True)),
                ('tel', models.CharField(max_length=20, null=True, blank=True)),
                ('address', models.CharField(max_length=200, null=True, blank=True)),
                ('site', models.CharField(max_length=200, null=True, blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
