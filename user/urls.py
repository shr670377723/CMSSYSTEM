from django.conf.urls import url
from user import views
urlpatterns=[
    url(r'^usertest/$',views.test),#用户添加
    url(r'^userAdd/$',views.userAdd),#用户添加
    url(r'^userQuery/$',views.userQuery),#用户查询
    url(r'^userQuery/1/',views.userQuery1),#用户查询
]