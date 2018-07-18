from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uphone = models.CharField(max_length=11,default='')
    uyoubian = models.CharField(max_length=6,default='')
    upeople = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.uname

class AddrInfo(models.Model):
    addr = models.CharField(max_length=100, default='')
    user = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.addr