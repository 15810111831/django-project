# coding:utf-8

from django.contrib.admin.sites import AdminSite


class MyAdminSite(AdminSite):
    site_header = '水果销售管理平台'
    site_title = '水果销售后台管理系统'


admin_site = MyAdminSite()
