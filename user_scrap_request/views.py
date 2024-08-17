from django.shortcuts import render
from  user_scrap_request.models import UserScrapRequest
import datetime
from django.core.files.storage import FileSystemStorage
# Create your views here.
def scrapdealer_view_user(request):
    obj = UserScrapRequest.objects.all()
    context = {
        'x': obj
    }
    return render(request,'user_scrap_request/scrapdealer_view_user_request.html',context)

def user_scrap(request,idd):
    uid=request.session["u_id"]
    if request.method == "POST":
        ob = UserScrapRequest()
        ob.vehicle_id=idd
        myfile=request.FILES['side1']
        fs=FileSystemStorage()
        file_name=fs.save(myfile.name,myfile)
        ob.photo_side1=myfile.name

        myfile = request.FILES['side2']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.photo_side2 = myfile.name

        myfile = request.FILES['side3']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.photo_side3 = myfile.name

        myfile = request.FILES['side4']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.photo_side4 = myfile.name

        ob.certificate_no=request.POST.get('certifi')
        ob.request_status='pending'
        ob.date=datetime.datetime.today()
        ob.time=datetime.datetime.now()
        ob.user_id=uid
        ob.save()


        message = "scrap request sent"
        context = {
            'msg': message
        }

        return render(request, 'temp/user.html', context)
    return render(request,'user_scrap_request/user_scrapping_request_reg.html')

def user_view_details(request):
    uid=request.session["u_id"]
    obj = UserScrapRequest.objects.filter(user_id=uid)
    context = {
        'x': obj
    }
    return render(request,'user_scrap_request/user_view_request_details.html',context)

