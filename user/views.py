#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from index.models import *
# Create your views here.
def userAdd(request):
    if request.method == 'GET':
        return render(request,'userAdd.html')
    else:
        uid = request.POST.get('sid','')
        upassword = request.POST.get('spwd','')
        uname = request.POST.get('sname','')
        # print(uid,uname,upassword)

        if uname and upassword and uid:
            try:
                Login.objects.get(uaccount=uid,upwd=upassword,uname=uname)
            except Login.DoesNotExist:
                login = Login(uaccount=uid,upwd=upassword,uname=uname)
                login.save()
                return render(request,'ok.html')
        return render(request,'file.html')
def userQuery(request):
    if request.method == 'GET':
        return render(request,'userQuery.html')
    else:
        uid = request.POST.get('sel','')
        both = request.POST.get('all','')
        if uid == 'stuid':
            login = Login.objects.filter(uaccount=both)
        elif uid == 'sname':
            login = Login.objects.filter(uname=both)
    return render(request,'userQuery.html',{'login':login})


def userQuery1(request):

        id= request.GET.get('qwert')
        print(id)
        if id:
            Login.objects.get(uaccount=id).delete()

            return render(request,'userQuery.html')
        return render(request,'userQuery.html')


def test(request):
    if request.method == 'GET':
        return render(request,'test.html')

    if request.method == 'POST':
        uname = request.POST.get('uname','')
        print(uname)
        return render(request,'test.html')

        # uname = request.POST.get('uname')
        # print(uname)
        # return render(request,'test.html')