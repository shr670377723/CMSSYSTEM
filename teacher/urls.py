from django.conf.urls import url
from teacher import views
urlpatterns=[
    url(r'^teaching/$',views.teaching),#教师任课
    url(r'^teachQuery/$',views.teachQuery),#任课教师查询
    url(r'^teachQuery/(.*)',views.teachQuery1),#任课教师查询
]