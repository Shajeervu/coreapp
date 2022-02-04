from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')
def Reportedissues(request):
    return render(request,'Reportedissues.html')
def reportissue(request):
    return render(request,'reportissue.html')
def reportedissue(request):
    return render(request,'reportedissue.html')
def TLsuccess(request):
    return render(request,'TLsuccess.html')
def issues(request):
    return render(request,'issues.html')