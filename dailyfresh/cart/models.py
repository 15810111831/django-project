# coding:utf-8
from django.db import models


class CartInfo(models.Model):
    user = models.ForeignKey('dj_user.UserInfo', verbose_name='用户')
    goods = models.ForeignKey('goods.GoodsInfo', verbose_name='商品')
    count = models.IntegerField('数量')
    total_price = models.DecimalField('总价', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'

    def save(self, *args, **kwargs):
        self.total_price = self.goods * self.count
        super(CartInfo, self).save(*args, **kwargs)

    def __str__(self):
        return self.count
