# coding:utf-8
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length = 20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length= 20)
    gpic = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=5, decimal_places=2) # max_digits 代表最大为数,包括小数位,decimal_places代表小数位的个数
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length = 20) # 单位
    gjieshao = models.CharField(max_length = 256)
    gclick = models.IntegerField(default=0)   # 按照点击率进行人气排序
    gkucun = models.IntegerField()   # 维护库存信息
    gcontent = HTMLField()   # 商品的详情信息
    gtype = models.ForeignKey(TypeInfo) #商品类别

    def __str__(self):
        return self.gtitle.encode('utf-8')