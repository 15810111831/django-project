# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-07 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_user', '0002_auto_20190307_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.Group', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xbb\x84'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission', verbose_name=b'\xe6\x9d\x83\xe9\x99\x90'),
        ),
    ]
