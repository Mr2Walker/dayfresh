# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-14 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodInfo',
            new_name='GoodsInfo',
        ),
    ]
