from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'type/(\d+)_(\d+)_(\d+)/$', views.type, name = 'type'),
    url(r'detail/(\d+)/(\d+)/$', views.detail, name = 'detail'),
]