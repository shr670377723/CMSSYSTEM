from django.conf.urls import url
from library import views
urlpatterns=[
    url(r'^bookInfo/$',views.bookInfo),#图书登记
    url(r'^bookMaintain/$',views.bookMaintain),#图书维护
    url(r'^bookMaintain/update/(.*)',views.bookupdate),#图书修改
    url(r'^bookBorrow/$',views.bookBorrow),#图书借阅
    url(r'^bookReturn/$',views.bookReturn),#图书归还
    url(r'^borrowQuery/$',views.borrowQuery),#借阅查询
]