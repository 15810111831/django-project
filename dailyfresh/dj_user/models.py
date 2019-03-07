# coding:utf-8
from django.db import models
from django.contrib.auth.models import Group, Permission


class UserInfo(models.Model):
    uname = models.CharField('用户名', max_length=20)
    upwd = models.CharField('密码', max_length=40)
    uemail = models.CharField('邮箱', max_length=30)
    uphone = models.CharField('电话', max_length=11, default='')
    uyoubian = models.CharField('邮编', max_length=6, default='')
    upeople = models.CharField('个人', max_length=10, default='')
    groups = models.ManyToManyField(Group, verbose_name='用户组', blank=True)
    user_permissions = models.ManyToManyField(Permission, verbose_name='权限', blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.uname


class AddrInfo(models.Model):
    addr = models.CharField(max_length=100, default='')
    user = models.ForeignKey(UserInfo)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = '地址信息'

    def __str__(self):
        return self.addr
