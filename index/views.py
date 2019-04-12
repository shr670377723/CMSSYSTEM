from django.http import HttpResponse
from django.shortcuts import render
from index.models import *
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd :
            Login.objects.filter(uaccount=uname,upwd=pwd)
            return render(request,'index.html',{'uname':uname})
        return HttpResponse('登录失败')


# def index(request):

    # return render(request,'index.html')
def index(request):
    return render(request,'index.html')