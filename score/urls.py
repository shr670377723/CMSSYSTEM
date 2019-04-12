from django.conf.urls import url
from score import views
urlpatterns=[
    url(r'teachCur/$',views.teachCur),#教师授课系统
    url(r'chooseCur/$',views.chooseCur),#学生选课系统
    url(r'^record/$',views.record),#成绩录入
    url(r'^query/$',views.query),#成绩查询
    url(r'^courseScore/$',views.courseScore),#班级成绩统计
]