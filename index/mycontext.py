#coding=utf-8
from django.shortcuts import render
from index.models import *
def mydata(request):

    from .models import Admissionsforms,Bookborrow,Bookinfo,Course,Clazz,Choosecur,Grade,Major,Stuinfo,Teacherinfo,Techcourse
    Admissionsforms = Admissionsforms.objects.all() #1学生入学登记
    Bookborrow = Bookborrow.objects.all()#2图书借阅
    Bookinfo = Bookinfo.objects.all()#3图书信息
    Choosecur = Choosecur.objects.all()#4学生选班
    Clazz = Clazz.objects.all()#5班级
    Course = Course.objects.all()#6课程
    Grade = Grade.objects.all()#7年级
    Major = Major.objects.all()#8专业
    Stuinfo = Stuinfo.objects.all()#9学生信息
    Teacherinfo =Teacherinfo.objects.all()#10教师信息
    Techcourse = Techcourse.objects.all()#11教师选班
    return {'Admissionsforms':Admissionsforms,'Bookborrow':Bookborrow,'Bookinfo':Bookinfo,
            'Choosecur':Choosecur,'Clazz':Clazz,'Course':Course,'Grade':Grade,'Major':Major,
            'Stuinfo':Stuinfo,'Teacherinfo':Teacherinfo,'Techcourse':Techcourse,
            }