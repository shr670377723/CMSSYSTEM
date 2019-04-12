from django.shortcuts import render
from index.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def majorCode(request):
    if request.method =='GET':
        all = Major.objects.all()
        return render(request,'majorCode.html',{'all':all})

    else:
        a = request.POST.dict()
        majorcode=request.POST.get('mid','')
        majorname = request.POST.get('mname','')
        if  majorcode=='' or majorname=='':
            return HttpResponse('不能为空')
        else:
            try:
                mid = Major.objects.get(mid=majorcode)
                return JsonResponse({'key':'2'})
            except Major.DoesNotExist:
                Major.objects.create(mid=majorcode,mname = majorname)
                all = Major.objects.all()
                return JsonResponse({'key':'1'})




def gradeCode(request):
    if request.method == 'GET':
        all = Grade.objects.all()
        return render(request,'gradeCode.html',{'all':all})
    else:
        gradecode = request.POST.get('gid','')
        gradename = request.POST.get('gname','')
        if gradecode =='' or gradename =='':
            return HttpResponse('不能为空')
        else:
            try:
                gid=Grade.objects.get(gid=gradecode)
            except Grade.DoesNotExist:
                Grade.objects.create(gid=gradecode,gname=gradename)
    all=Grade.objects.all()
    return render(request,'gradeCode.html',{'all':all})

def classCode(request):
    if request.method == 'GET':
        all = Clazz.objects.all()
        return render(request, 'classCode.html',{'all':all})
    else:
        print('22222222222222')
        majorname = request.POST.get('mname')
        gradename = request.POST.get('gname')
        classname = request.POST.get('cname')
        try:
            major=Major.objects.get(mname=majorname)
        except Major.DoesNotExist:
            major=Major.objects.create(mname=majorname)
        try:
            grade=Grade.objects.get(gname=gradename)
            print('创建年级')
        except Grade.DoesNotExist:
            gra = request.POST.get('gname')[:-1]
            print(gra)
            gra=int(gra)
            grade=Grade.objects.create(gname=gradename,gid=gra)
        try:
            classname = Clazz.objects.get(cname=classname)
        except Clazz.DoesNotExist:
            cla=Clazz.objects.create(gid=grade,cname=classname,mid=major)
    all = Clazz.objects.all()
    return render(request, 'classCode.html', {'all': all})




def subjectCode(request):
    if request.method =='GET':
        all = Course.objects.all()
        return render(request,'subjectCode.html',{'all':all})
    else:
        id = request.POST.get('curid')
        id = int(id)
        cname = request.POST.get('curname','')
        curdata = request.POST.get('examdate','')
        curtype = request.POST.get('examtype','')
        try:
            Course.objects.get(curid=id)
        except Course.DoesNotExist:
            Course.objects.create(curid=id,curname=cname,examdate=curdata,examtype=curtype)
    all = Course.objects.all()
    return render(request, 'subjectCode.html',{'all':all})

def majordelete(request,num):
    print(num)
    try:
        Clazz.objects.get(cid=num).delete()
    except:
        Major.objects.get(mid=num).delete()
    all = Major.objects.all()
    return render(request,'majorCode.html',{'all':all})


def gradedelete(request,num):
    try:
        Clazz.objects.get(cid=num).delete()
    except:
        Grade.objects.get(gid=num).delete()
    all = Grade.objects.all()
    return render(request, 'gradeCode.html', {'all': all})


def majorupdate(request,num,name):
    if request.method=='GET':
        all =Major.objects.get(mid=num,mname=name)
        return render(request, 'majorupdate.html', {'all':all})
    else:
        mcode = request.POST.get('mid')
        print(mcode)
        majorname= request.POST.get('mname')
        print(majorname)
        # Major.objects.filter(mid=num,mname=name).update(mid=mcode,mname=majorname)
        Major.objects.filter(mid=num).update(mid=mcode,mname=majorname)
    all = Major.objects.all()
    return render(request,'majorCode.html',{'all':all})



def gradeupdate(request,num):
    if request.method =='GET':
        all = Grade.objects.get(gid=num)
        return render(request,'gradeupdate.html',{'all':all})
    else:
        gcode = request.POST.get('gid')
        gradername = request.POST.get('gname')
        Grade.objects.filter(gid=num).update(gid=gcode,gname=gradername)
    all = Grade.objects.all()
    return render(request, 'gradeCode.html', {'all': all})


def subjectdelete(request,num):
        Course.objects.get(curid=num).delete()
        all = Course.objects.all()
        return render(request, 'subjectCode.html', {'all': all})


def classdelete(request,num):
    Clazz.objects.filter(cid=num).delete()
    all = Clazz.objects.all()
    return render(request,'classCode.html',{'all':all})


def subjectupdate(request,num):
    if request.method == 'GET':
        all = Course.objects.all()
        return render(request,'subjectupdate.html',{'all':all})
    else:
        cid= request.POST.get('curid')
        cname= request.POST.get('curname')
        cdate=request.POST.get('examdate')
        cid=int(cid)
        Course.objects.filter(curid=num).update(curid=cid,curname=cname,examdate=cdate)
    all = Course.objects.all()
    return render(request,'subjectCode.html',{'all':all})


