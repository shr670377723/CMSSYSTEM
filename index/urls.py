#coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.login),  #登录
    url(r'^index/',views.index),  #登录

]