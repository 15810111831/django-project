# coding:utf-8

from django.contrib.admin.sites import AdminSite


class MyAdminSite(AdminSite):
    site_header = '天天生鲜管理平台'
    site_title = '天天生鲜后台管理系统'


admin_site = MyAdminSite()
