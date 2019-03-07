# coding: utf-8

from common import admin_site
from .models import UserInfo
from django.contrib.auth.models import Group, Permission

admin_site.register(UserInfo)
admin_site.register(Group)
admin_site.register(Permission)


# Register your models here.
