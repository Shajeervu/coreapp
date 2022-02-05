from django.http import request
from django.shortcuts import render

# Create your views here.
def devindex(request):
    return render(request,'devindex.html')
def devdashboard(request):
    return render(request,'devdashboard.html')
def devReportedissues(request):
    return render(request,'devReportedissues.html')
def devreportissue(request):
    return render(request,'devreportissue.html')
def devreportedissue(request):
    return render(request,'devreportedissue.html')
def devsuccess(request):
    return render(request,'devsuccess.html')
def devissues(request):
    return render(request,'devissues.html')
def devsample(request):
    return render(request,'devsample.html')