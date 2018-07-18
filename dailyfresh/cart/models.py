from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey('dj_user.UserInfo')
    goods = models.ForeignKey('goods.GoodsInfo')
    count = models.IntegerField()

    def __str__(self):
        return self.count
