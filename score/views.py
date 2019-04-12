from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from index.models import *
# Create your views here.

def teachCur(request):
    if request.method == 'GET':
        # print('')
        tid = request.GET.get('tid','0')
        if tid and Teacherinfo.objects.filter(tid=tid):
            print('---------------------')
            courses = Course.objects.all()
            return render(request,'teachCur.html',{'tid':tid,'courses':courses})
        else:
            # info = '系统查找不到该信息'
            return render(request,'teachCur.html',{'tid':tid})

    else:
        tid = request.POST.get('tid','')
        print(tid)
        curids = request.POST.getlist('ccourse','')#获取所选课程id
        for curid in curids:
            try:
                Techcourse.objects.get(tid__tid=tid,curid__curid=curid)
            except Techcourse.DoesNotExist:
                teacher = Teacherinfo.objects.get(tid=tid)
                course = Course.objects.get(curid=curid)
                tc = Techcourse.objects.create(tid=teacher,curid=course)
                tc.save()
        return HttpResponse('提交成功')



def chooseCur(request):
    if request.method == 'GET':
        stuid = request.GET.get('sid','0')

        if stuid and Admissionsforms.objects.filter(sid=stuid):
            courses = Techcourse.objects.all()
            return render(request,'chooseCur.html',{'cur_list':courses,'stuid':stuid})
        else:
            # info = '系统查找不到该信息'
            return render(request, 'chooseCur.html')

    else:
        stuid = request.POST.get('sid', '')
        curids = request.POST.getlist('cbutton','')#获取所选课程的课程id
        for curid in curids:
            try:
                Choosecur.objects.get(curid__curid=curid,sid__sid__sid=stuid)
            except Choosecur.DoesNotExist:
                stu = Stuinfo.objects.get(sid_id=stuid)
                cur = Course.objects.get(curid=curid)
                cc = Choosecur.objects.create(sid=stu,curid=cur)
                cc.save()
        return HttpResponse('提交成功')


import json
from django.core.serializers import serialize
import jsonpickle
def record(request):
    if request.method == 'GET':
        stuid = request.GET.get('sid', '0')

        if stuid and Admissionsforms.objects.filter(sid=stuid):
            stuList = Choosecur.objects.filter(sid_id=stuid)
            # stuList = serialize('json',stuList)
            # stuList = jsonpickle.dumps(stuList)
            # return  JsonResponse({'stuid':stuid,'courses':stuList})
            return render(request,'record.html',{'courses':stuList,'stuid':stuid})
        else:
            return render(request, 'record.html')
    else:
        params = request.POST.dict()
        stuid = params.pop('sid')
        params.pop('csrfmiddlewaretoken')
        for a,b in params.items():
            print(a,b)
            Choosecur.objects.filter(sid_id=stuid, curid_id=a).update(score = b)
        return render(request,'record.html')


def query(request):
    option = request.POST.get('sel','')
    condition = request.POST.get('condition','')
    if option == 'sid':
        if condition.isdigit() and Admissionsforms.objects.filter(sid=condition):
            stus = Choosecur.objects.filter(sid_id=condition)
            return render(request,'query.html',{'stus':stus})
        else:
            return render(request, 'query.html')
    else:
        if condition and Admissionsforms.objects.filter(sname=condition):
            queryset = []
            #重名问题
            stu = Admissionsforms.objects.filter(sname=condition)
            for s in stu:
                sid = s.sid
                stus = Choosecur.objects.filter(sid_id=sid)
                queryset.extend(stus)
            print(queryset)
            return render(request, 'query.html', {'stus': queryset})
        else:
            return render(request, 'query.html',)


def courseScore(request):
    cur_list = []
    cur = Course.objects.all()  # 获取所有班级
    for c in cur:
        # print(c)
        cur_list.append(c.curname)
    if request.method == 'GET':
        return render(request, 'courseScore.html', {'cur_list':cur_list})
    else:
        curname = request.POST.get('sel','')#获取所选班级
        examtype = request.POST.get('examtype','')
        examdate = request.POST.get('examdate','')
        cc=''
        if curname:
            if examtype:
                if examdate:
                    cc = Choosecur.objects.filter(curid__curname=curname, curid__examdate=examdate,
                                                  curid__examtype=examtype)
                else:
                    cc = Choosecur.objects.filter(curid__curname=curname,curid__examtype=examtype)
            else:
                if examdate:
                    cc = Choosecur.objects.filter(curid__curname=curname, curid__examdate=examdate)
                else:
                    cc = Choosecur.objects.filter(curid__curname=curname)

        else:
            if examtype:
                if examdate:
                    cc = Choosecur.objects.filter( curid__examdate=examdate,curid__examtype=examtype)
                else:
                    cc = Choosecur.objects.filter(curid__examtype=examtype)
            else:
                if examdate:
                    cc = Choosecur.objects.filter(curid__examdate=examdate)
                else:
                    pass


    # if curname and examdate and examtype:
    #     cc = Choosecur.objects.filter(curid__curname=curname,curid__examdate=examdate,curid_examtype=examtype)
    # elif examdate and not examtype:
    #     cc = Choosecur.objects.filter(curid__curname=curname,curid__examdate=examdate)
    # elif not examdate and examtype:
    #     cc = Choosecur.objects.filter(curid__curname=curname,curid__examtype=examtype)
    # else:
    #     cc = Choosecur.objects.filter(curid__curname=curname)
    return render(request, 'courseScore.html', {'cur_list':cur_list, 'cc':cc})

