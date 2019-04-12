from django.conf.urls import url
from archive import views
urlpatterns=[
    url(r'^stuInfo/$',views.stuInfo),#学生基本信息
    url(r'^stuCheckIn/$',views.stuCheckIn),#学生入校登记
    url(r'^stuInfoMaintain/$',views.stuInfoMaintain),#学生信息维护
    url(r'^stuRegQuery/$',views.stuRegQuery),#学生登记查询
    url(r'^teachInfo/$',views.teachInfo),#教师信息
    url(r'^teachInfoMt/$',views.teachInfoMt),#教师信息维护
    url(r'^teachInfo/update/',views.update),#教师信息维护变更
    url(r'^stuInfo/update/(.*)$',views.supdate),#学生基本信息变更
]