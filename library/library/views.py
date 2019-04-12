from django.shortcuts import render

# Create your views here.
from index.models import *


def bookInfo(request):
    if request.method == 'GET':
        return render(request,'bookInfo.html')
    else:
        # print(request.POST.dict())
        sh = request.POST.get('bid')
        sm = request.POST.get('bname')
        zz = request.POST.get('author')
        lb = request.POST.get('category')
        cbs = request.POST.get('publication')
        fxrq = request.POST.get('pubdate')
        czy = request.POST.get('operator')
        jg = request.POST.get('price')
        rksl = request.POST.get('bnum')
        rksj = request.POST.get('indate')
        tsjj = request.POST.get('intro')
        many = (sh,sm,zz,lb,cbs,fxrq,czy,jg,rksj,rksl,tsjj)
        # print(many)
        # for a in many:
        #     print(a+'-')
        l=[1,'',2]
        print(len(l))
        if many:
                #     print('1')
                # else:
                #     # ('', '', '', '', '', '', '', '', '', '', '')
                #     return render(request, 'file.html')
            try :
               bk = Bookinfo.objects.get(bid=sh,bname=sm,author=zz,category=lb,publication=cbs,pubdate=fxrq,bnum=rksl,indate=rksj,price=jg,intro=tsjj,operator=czy)
            except:
               bk = Bookinfo.objects.create(bid=sh,bname=sm,author=zz,category=lb,publication=cbs,pubdate=fxrq,bnum=rksl,indate=rksj,price=jg,intro=tsjj,operator=czy)
                # bk.save()
            return render(request,'ok.html')

def bookMaintain(request):
    return render(request,'bookMaintain.html')


def bookBorrow(request):
    return render(request,'bookBorrow.html')


def bookReturn(request):
    if request.method == 'GET':
        borrow = Bookborrow.objects.all()
        return render(request,'bookReturn.html',{'borrow':borrow})
    else:
        sid = request.POST.get('sid')
        sname = request.POST.get('sname')
        bid = request.POST.get('bid')
        bname = request.POST.get('bname')
        borrowdate = request.POST.get('borrowdate')
        many = (sid,sname,bid,bname,borrowdate)
        if many:
            Bookborrow.objects.get(bid=bid).delete()
        borrow = Bookborrow.objects.all()
        return render(request, 'bookReturn.html',{'borrow':borrow})
def borrowQuery(request):
    if request.method == 'GET':
        return render(request,'borrowQuery.html')
    else:
        select = request.POST.get('select')
        al = request.POST.get('all')
        # print(select,al)
        if select == 'xh':
            cx = Bookborrow.objects.filter(sid=al)
            # print(cx)
        elif select == 'sh':
            cx = Bookborrow.objects.filter(bid=al)
            # print(cx)
        elif select == 'jyrq':
            cx = Bookborrow.objects.filter(borrowdate=al)
        return render(request,'borrowQuery.html',{'cx':cx})