# coding:utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *
import hashlib

def register(request):
    return render(request, 'dj_user/register.html')


def register_handle(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        upwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        uemail = request.POST['email']

        # 判断两次密码是否相等
        if upwd != cpwd:
            return redirect(reverse('user:register'))

        # 密码加密
        sh1 = hashlib.sha1()
        sh1.update(upwd)
        upwd3 = sh1.hexdigest()
        user = UserInfo()
        user.uname = uname
        user.upwd = upwd3
        user.uemail = uemail
        user.save()
        return redirect('/user/login/')

# 验证用户名是否存在
def register_exist(request):
    uname = request.GET['uname']
    count = UserInfo.objects.filter(uname = uname).count()
    print count
    return JsonResponse({'count':count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登陆','error_name':0, 'error_pwd':0 ,'uname':uname, 'upwd':''}
    return render(request, 'dj_user/login.html', context)

def login_handle(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    jizhu = request.POST.get('jizhu',0)
    # 根据获取的uname查询数据库,如果存在用户则验证密码
    # 这里选择用filter查询的原因是因为get查询如果没有找到值则会报错,用filter如果没查到则返回空列表
    users = UserInfo.objects.filter(uname = uname)
    print uname
    if len(users) == 1:
        s1 = hashlib.sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            # 如果用户记住用户名了,则设置cookie保存用户名
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                # 设置过期时间为-1 表示立马过期
                red.set_cookie('uname', '',max_age=-1)

            # 设置会话存储,因为很多由用户绑定的信息,而且需要在页面上显示用户名信息
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            # 如果密码不正确
            context = {'title': '用户登录', 'error_name':0, 'error_pwd':1, 'uname':uname, 'upwd':upwd}
            return render(request, 'dj_user/login.html', context)
    else:
        # 如果用户名错误
        context = {'title': '用户登陆', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'dj_user/login.html', context)

def info(request):
    print request.session['user_id']
    user_email = UserInfo.objects.get(id = request.session['user_id']).uemail
    context = {'title':'用户中心', 'user_email': user_email, 'user_name': request.session['user_name'],'page_name':1}
    return render(request, 'dj_user/user_center_info.html', context)

def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'GET':
        print user
    else:
        user.uphone = request.POST['uphone']
        user.uyoubian = request.POST['uyoubian']
        user.upeople = request.POST['upeople']
        addr = request.POST['addr']
        addrinfo = AddrInfo()
        print addrinfo
        addrinfo.addr = addr
        addrinfo.user = user
        user.save()
        addrinfo.save()
    user_addrs = user.addrinfo_set.filter(user_id = user.id)
    if len(user_addrs) == 0:
        user_addr = ''
    else:
        user_addr = user_addrs[0].addr

    context = {'title':'用户中心', 'user':user,'addr':user_addr}
    return render(request, 'dj_user/user_center_site.html', context)

def order(request):
    return render(request, 'dj_user/user_center_order.html')