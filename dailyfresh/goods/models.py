# coding:utf-8
from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    name = models.CharField('类别名称', max_length=20)
    isDelete = models.BooleanField('是否删除', default=False)

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = '商品类别'

    def __str__(self):
        return self.name.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField("商品名称", max_length=20)
    gpic = models.ImageField('商品图片', upload_to='goods/')
    # max_digits 代表最大为数,包括小数位,decimal_places代表小数位的个数
    gprice = models.DecimalField('商品价格', max_digits=5, decimal_places=2)
    isDelete = models.BooleanField('是否删除', default=False)
    gunit = models.CharField('单位', max_length=20)  # 单位
    gjieshao = models.CharField('简介', max_length=256)
    gclick = models.IntegerField('点击率', default=0)   # 按照点击率进行人气排序
    gkucun = models.IntegerField('库存')   # 维护库存信息
    gcontent = HTMLField('商品详情信息')   # 商品的详情信息
    gtype = models.ForeignKey(TypeInfo, verbose_name='商品类别')  # 商品类别

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'

    def __str__(self):
        return self.gtitle
