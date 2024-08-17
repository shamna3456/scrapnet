from django.shortcuts import render
from login.models import Login
# Create your views here.
def admin(request):
    return render(request, 'temp/admin.html')

def home(request):

    return render(request,'temp/home.html')

def police(request):
    return render(request,'temp/police.html')

def RTO(request):
    return render(request,'temp/rto.html')

def scrapdealer(request):
    return render(request,'temp/scrapdealer.html')

def user(request):
    return render(request,'temp/user.html')