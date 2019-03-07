# coding:utf-8

from common import admin_site
from django.contrib import admin
from .models import TypeInfo, GoodsInfo


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['name']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle', 'gprice', 'gcontent', 'gtype']


admin_site.register(TypeInfo, TypeInfoAdmin)
admin_site.register(GoodsInfo, GoodsInfoAdmin)
