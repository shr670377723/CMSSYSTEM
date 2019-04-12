# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from index.models import *


def teaching(request):
    from index.models import Techcourse
    t = Techcourse.objects.all()
    if request.method == 'GET':

        return render(request, 'teaching.html',{'t':t})
    else:
        tidd = request.POST.get('tid')
        course = request.POST.get('course')
        tc = ''
        print(tidd)
        print(course)
        if tidd:
            if course:
                tc = Techcourse.objects.filter(tid=tidd,curid=course)
            else:
                tc = Techcourse.objects.filter(tid=tidd)
            return render(request, 'teaching.html', {'tc': tc,'t':t})
        else:
            if course:
                tc = Techcourse.objects.filter(curid=course)
            else:
                pass
    return render(request, 'teaching.html',{'t':t,'tc':tc})


def teachQuery(request):
    if request.method == 'GET':
        return render(request, 'teachQuery.html')
    else:
        cid = request.POST.get('sel', '')
        both = request.POST.get('all', '')
        print(cid,both)
        if cid == 'curid':
            login = Course.objects.filter(curname=both)
            print(login)
            tlist = []
            for i in login:
                curid = i.curid
                # print(curid)
                tid = Techcourse.objects.filter(curid__curid=curid)
                for j in tid:
                    teachid = j.tid
                    tlist.append(teachid)
            return render(request, 'teachQuery.html', {'teachid': tlist, 'login':login})

        elif cid == 'tname':
            ttid = Teacherinfo.objects.filter(tname=both)
            # print(ttid)
            list = []
            for k in ttid:
                # print(k)
                tid = k.tid
                print(tid)
                teachcourse = Techcourse.objects.filter(tid__tid=tid)
                # print(teachcourse)
                for l in teachcourse:
                    # print(l)
                    cuorseid = l.curid
                    a=cuorseid.curname
                    # print(a)
                    list.append(cuorseid)

        return render(request, 'teachQuery.html', {'teachid': ttid, 'login': list})

def teachQuery1(request,num):
        b = Techcourse.objects.filter(tid=num)
        for j in b:
            cur = j.curid.curid

        a = Teacherinfo.objects.filter(tid=num)
        for i in a:
            cid = i.mid.mid
            # print(cid)
        Techcourse.objects.get(tid=num).delete()
        # Major.objects.get(mid=cid).delete()
        Teacherinfo.objects.get(tid=num).delete()


        Course.objects.get(curid=cur).delete()



        return render(request, 'teachQuery.html')
