# coding:utf-8
from django.db import models


class UserInfo(models.Model):
    uname = models.CharField('用户名', max_length=20)
    upwd = models.CharField('密码', max_length=40)
    uemail = models.CharField('邮箱', max_length=30)
    uphone = models.CharField('电话', max_length=11, default='')
    uyoubian = models.CharField('邮编', max_length=6, default='')
    upeople = models.CharField('个人', max_length=10, default='')

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
