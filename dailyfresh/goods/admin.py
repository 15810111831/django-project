from django.contrib import admin
from .models import TypeInfo, GoodsInfo


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['name']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle', 'gprice', 'gcontent', 'gtype']


admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
