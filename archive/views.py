from django.core import serializers
from django.http import HttpResponse, response, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.template import Template, Context
# Create your views here.



def stuInfo(request):
    if request.method == 'GET':
        return render(request,'stuInfo.html')
    else:
        from index.models import Stuinfo,Admissionsforms
        # b =request.getPa
        a = request.POST.dict()
        a.pop('csrfmiddlewaretoken')
        a = a.items()
        l = []
        for _,a in a:
            l.append(a)
        l = tuple(l)
        # print(l)
        cls,sid,sname,gender,age,sidnum,sbirthdate,saddress,sphone,politicstatus,health=l
        # print(sid)
        try:
            Stuinfo.objects.get(sid__sid=sid)
            Stuinfo.objects.filter(sid__sid=sid).update(**
            {'sid':Admissionsforms.objects.get(sid=sid),'identitynum':sidnum,
             'gender':gender,'birthdate':sbirthdate,'address':saddress,
             'age':age,'tel':sphone,'politicstatus':politicstatus,'health':health})
            # return JsonResponse({'key':'2'})
            return render(request,'stuInfoMaintain.html')
            # print('更改')
        except:
            # print('创建')
            Stuinfo.objects.create(**{'sid':Admissionsforms.objects.get(sid=sid)
                ,'identitynum':sidnum,'gender':gender,'birthdate':sbirthdate,'address':saddress,
                'age':age,'tel':sphone,'politicstatus':politicstatus,'health':health})
            # print('添加成功')
            return JsonResponse({'key':'1'})



def supdate(request,num):
    from index.models import Stuinfo,Clazz,Admissionsforms
    stu = Stuinfo.objects.get(sid__sid=num)
    Clazz = Clazz.objects.all()
    return render(request, 'stuInfoupdate.html',{'stu':stu,'Clazz':Clazz})



def stuCheckIn(request):
    if request.method =='GET':
        return render(request,'stuCheckIn.html')
    else:
        from index.models import Clazz
        a = request.POST.dict()
        a.pop('csrfmiddlewaretoken')
        print(a)
        a = a.items()
        l = []
        for _, a in a:
            l.append(a)
        l = tuple(l)
        print(l)
        sid, sname, cname, mname, indate, agent, inscore=l
        # sid = request.POST.get('sid','007')#学生编号
        # sname = request.POST.get('sname','007')#学生姓名
        # cname = request.POST.get('cname','007')#班级名称
        # mname = request.POST.get('mname','007')#专业名称
        # indate = request.POST.get('indate','007')#入学日期
        # agent = request.POST.get('agent','007')#经办人
        # inscore = request.POST.get('inscore','007')#入学分数
        print('%s,%s,%s,%s,%s,%s,%s'%(sid,sname,cname,mname,indate,agent,inscore))
        gdate = int(indate[:4])

        from index.models import Admissionsforms,Clazz,Grade,Major
        try:
            Major.objects.get(mname=mname)
        except:
            Major.objects.create(mname=mname)#创建专业
            # print('创建专业')

        try:
            Grade.objects.get(gid=gdate)
        except:
            Grade.objects.create(**{'gid':gdate,'gname':'%s'%(str(gdate)+'级')})#创建年级
        try:
            grade = Grade.objects.get(gid=gdate)
            major = Major.objects.get(mname=mname)
            Clazz.objects.get(cname=str(grade.gid)+str(major.mid)+cname)
        except:
            # cls = Clazz()
            major = Major.objects.get(mname=mname)
            grade = Grade.objects.get(gid=gdate)
            Clazz.objects.create(**{'cname':str(grade.gid)+str(major.mid)+cname,'gid':Grade.objects.get(gid=gdate),'mid':Major.objects.get(mname=mname)})
        try:
            from index.models import Grade, Major
            grade = Grade.objects.get(gid=gdate)
            major = Major.objects.get(mname=mname)
            cls = Clazz.objects.get(cname=str(grade.gid) + str(major.mid) + cname)
            sid = indate[2:4] + str(major.mid) + str(cls.cid) + sid
            Admissionsforms.objects.get(sid=sid)
            return JsonResponse({'key':'2'})
        except:

            ad = Admissionsforms()
            ad.sid=sid
            ad.cname=cls
            ad.sname=sname
            ad.indate=indate
            ad.inscore=inscore
            ad.agent=agent
            ad.save()
            print('>>???')
            return JsonResponse({'key': '1'})
        # messages.success(request, '添加成功')
        # return JsonResponse({'key':'2'})
    # messages.error(request, '添加失败')
    # return render(request,'stuCheckIn.html')


def stuInfoMaintain(request):

    if request.method =='GET':
        return render(request, 'stuInfoMaintain.html')
    else:
        import pickle
        from index.models import Admissionsforms,Stuinfo
        condition = request.POST.get('condition','')
        qcondition=request.POST.get('qconditon','')
        print(condition)
        print(qcondition)
        stu = 0
        ad = 0
        if qcondition=='sid':
            stu = Stuinfo.objects.get(sid=condition)
        elif qcondition=='sname':
            ad = Admissionsforms.objects.filter(sname=condition)
            stu = []
            for ad in ad:
                stu.append(Stuinfo.objects.get(sid=ad.sid))
        elif qcondition=='identityNum':
            stu = Stuinfo.objects.filter(identitynum__contains=condition)
        try:
            iter(stu)
        except:
            stu = [stu,'']


        # stu = serializers.serialize("json", stu)
        # ad = serializers.serialize("json", ad)
        # return JsonResponse({'key':1,'stu':stu,'ad':ad})
        return render(request, 'stuInfoMaintain.html', {'stu': stu})



def stuRegQuery(request):
    if request.method =='GET':
        return render(request, 'stuRegQuery.html')
    else:
        from index.models import Admissionsforms,Stuinfo
        condition = request.POST.get('condition','')
        qcondition=request.POST.get('qconditon','')
        oc = request.POST.get('oc','')
        stu = []
        if qcondition=='sid':
            if oc=='__gt':
                # q = qcondition+'__sid'+oc
                # print(q)
                stu = Stuinfo.objects.filter(sid__sid__gt=condition)
            elif oc == '__lt':
                stu = Stuinfo.objects.filter(sid__sid__lt=condition)
            elif oc == '==':
                stu = Stuinfo.objects.get(sid__sid__exact=condition)
            elif oc == '__gte':
                stu = Stuinfo.objects.filter(sid__sid__gte=condition)
            elif oc == '__lte':
                stu = Stuinfo.objects.filter(sid__sid__lte=condition)
            try:
                iter(stu)
            except:
                stu = ['',stu]
        elif qcondition=='indate':
            def sizeOfDate(oc):
                from django.db import connection
                cursor = connection.cursor()
                # print("SELECT * from admissionsforms where DATE_FORMAT(indate,'%Y%m%d') >"+condition)
                cursor.execute("SELECT * from admissionsforms where DATE_FORMAT(indate,'%Y%m%d')"+oc + condition)
                a = cursor.fetchall()
                for a in a:
                    stu.append(Stuinfo.objects.get(sid=a[0]))
            if oc == '__gt':
                sizeOfDate('>')
            elif oc == '__lt':
                sizeOfDate('<')
            elif oc == '==':
                sizeOfDate('=')
            elif oc == '__gte':
                sizeOfDate('>=')
            elif oc == '__lte':
                sizeOfDate('<=')
        elif qcondition=='inscore':
            condition=str('%.2f'%float(condition))#如果先转整形会出现输入小数无法转换为整数
            def sizeOfIndate(oc):
                from django.db import connection
                cursor = connection.cursor()
                cursor.execute("SELECT * from admissionsforms where inscore"+oc + condition)
                ab = cursor.fetchall()
                for a in ab:
                    stu.append(Stuinfo.objects.get(sid=a[0]))
            if oc == '__gt':
                sizeOfIndate('>')
            elif oc == '__lt':
                sizeOfIndate('<')
            elif oc == '==':
                sizeOfIndate('=')
            elif oc == '__gte':
                sizeOfIndate('>=')
            elif oc == '__lte':
                sizeOfIndate('<=')
        return render(request, 'stuRegQuery.html', {'stu': stu})



def teachInfo(request):
    if request.method=='GET':
        from index.models import Major
        major = Major.objects.all()
        return render(request,'teachInfo.html',{'major':major})
    else:
        from index.models import Teacherinfo,Major
        a = request.POST.dict()
        a.pop('csrfmiddlewaretoken')
        # print(type(a))
        a = a.items()
        l1 = []
        for _, y in a:
            l1.append(y)
        l1 = tuple(l1)
        tname, tage, gender, marry, status, nation, edbackground, birthday, tidnum, tphone, tdate, tcourse, work = l1
        try:
            Teacherinfo.objects.get(idnum=tidnum)
            Teacherinfo.objects.filter(idnum=tidnum).update(**{'mid':Major.objects.get(mid=tcourse),'tname':tname,'gender':gender,'age':tage,'married':marry,'idnum':tidnum,'politicstatus':status,'nation':nation,'edu':edbackground,'birthdate':birthday,'tel':tphone,'workdate':tdate,'description':work})
        except:
            Teacherinfo.objects.create(**{'mid':Major.objects.get(mid=tcourse),'tname':tname,'gender':gender,'age':tage,'married':marry,'idnum':tidnum,'politicstatus':status,'nation':nation,'edu':edbackground,'birthdate':birthday,'tel':tphone,'workdate':tdate,'description':work})
    return render(request,'teachInfo.html')



def teachInfoMt(request):
    if request.method == 'GET':
        return render(request,'teachInfoMt.html')
    else:
        from index.models import Teacherinfo,Major
        a = request.POST.dict()
        a.pop('csrfmiddlewaretoken')
        a = a.items()
        b=[]
        for _,a in a:
            b.append(a)
        b=tuple(b)
        qcondition,condition=b
        if qcondition == 'tname':
            teacher = Teacherinfo.objects.filter(tname=condition)
        elif qcondition =='tcourse':
            teacher = Teacherinfo.objects.filter(mid=Major.objects.get(mname=condition))
        else:
            teacher = Teacherinfo.objects.filter(idnum__contains=condition)
    return render(request,'teachInfoMt.html',{'teacher':teacher})


def update(request):
    tid = request.GET.get('id','')
    from index.models import Teacherinfo,Major
    teacher = Teacherinfo.objects.get(tid=tid)
    major = Major.objects.all()
    return render(request, 'teacherupdate.html',{'teacher':teacher,'major':major})