from django.shortcuts import render

# Create your views here.
def sysInfo(request):
    return render(request,'sysInfo.html')
