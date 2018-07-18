# coding:utf-8
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def index(request):
    #  想要显示所有的类别以及类别下的热门商品,和每个类的商品信息
    types = TypeInfo.objects.all()
    context = {'title':u'首页'}
    i = 0
    goods = GoodsInfo.objects.all()
    context['types'] = types
    context['goods'] = goods
    context['guest_cart'] = 1
    return render(request, 'goods/index.html', context)

def type(request, typeId, pindex, sort):
    # 列表页需要显示的东西: 商品列表(需要分页),最新推荐,按照人气等排序
    types = TypeInfo.objects.all()
    type = TypeInfo.objects.get(pk = typeId)
    news = type.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':
        # 默认排序
        goods_list = GoodsInfo.objects.filter(gtype_id = typeId).order_by('-id')
    elif sort == '2':
        # 价格排序
        goods_list = GoodsInfo.objects.filter(gtype_id = typeId).order_by('-gprice')
    elif sort == '3':
        # 人气排序
        goods_list = GoodsInfo.objects.filter(gtype_id = typeId).order_by('-gclick')
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(pindex))
    plist = paginator.page_range
    index = pindex
    context = {'title':type.ttitle, 'page':page, 'types':types,
               'type':type, 'goods_list':goods_list, 'news':news , 'sort':sort , 'plist':plist, 'index':index,'guest_cart':1}
    return render(request,'goods/list.html', context )

def detail(request, typeId, goodId):
    types = TypeInfo.objects.all()
    type = TypeInfo.objects.get(pk = typeId)
    good = GoodsInfo.objects.get(id = goodId)
    news = GoodsInfo.objects.filter(gtype_id = typeId).order_by('-id')[:2]
    context = {'title':good.gtitle, 'good':good,'guest_cart':1, 'types':types, 'news':news , 'type':type ,'guest_cart':1}
    return render(request, 'goods/detail.html', context)