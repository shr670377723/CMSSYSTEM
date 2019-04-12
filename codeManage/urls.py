from django.conf.urls import url
from codeManage import views
urlpatterns=[
    url(r'^majorCode/$',views.majorCode),#专业代码维护
    url(r'^gradeCode/$',views.gradeCode),#年级代码维护
    url(r'^classCode/$',views.classCode),#班级代码维护
    url(r'^subjectCode/$',views.subjectCode),#学科代码维护
    url(r'^majorCode/delete/(.*)',views.majordelete),#专业删除
    url(r'^gradeCode/delete/(.*)',views.gradedelete),#年级删除
    url(r'^majorCode/update/(?P<num>.*)/(?P<name>.*)/',views.majorupdate),#跳转专业更改页面及传参
    url(r'^gradeCode/update/(.*)',views.gradeupdate),#年级更改
    url(r'^subjectCode/update/(.*)',views.subjectupdate),#学科更改
    url(r'^subjectCode/delete/(.*)', views.subjectdelete),  # 学科删除
    url(r'^classCode/delete/(.*)', views.classdelete),  # 班级删除
]