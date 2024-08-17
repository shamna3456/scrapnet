from django.shortcuts import render
from station_vehicle.models import StationVehicle
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone
from datetime import timedelta
def station(request):
    uid=request.session["u_id"]
    if request.method=="POST":
        ob=StationVehicle()
        ob.owner_name = request.POST.get('name')
        ob.vehicle_num = request.POST.get('vehicle_no')
        ob.email=request.POST.get('mail')
        ob.starting_date = request.POST.get('startDate')
        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.expiry_date= timezone.now() + timedelta(days=5*365)
        ob.police_station_id='1'
        ob.photo = myfile.name
        ob.status=' '
        ob.save()
    # return render(request, 'temp/police_home.html')


    return render(request,'station_vehicle/scrap_station_vehicle.html')


def view_stationvehicle(request):
    obj = StationVehicle.objects.all()
    cdt = timezone.now()
    cdate = cdt.date()
    for oo in obj:
        if oo.expiry_date < cdate:
            oo.status='Expired'
            oo.save()
    context = {
        'x': obj
    }
    return render(request,'station_vehicle/view_station_vehicle.html',context)

import smtplib
def send_mail(request,idd):
    ob=StationVehicle.objects.get(station_vehicle_id=idd)
    email = "projectmailbg@gmail.com"
    # scount = int(ob.suspicious_count)


    msg = "Vehicle Vehicle No: " + ob.vehicle_num + ' has Expired and need to scrap .Collect the vehicle as soon as possible... '
    try:
        em="shamnakuppattil@gmail.com"
        sub = "Scrap Request. Vehicle Expiry"
        text = f'subject : {sub} \n\n{msg}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, 'iqjjrhsyerovorav')
        server.sendmail(email, str(em), text)
        message="send"
        # return HttpResponseRedirect('/check/check/')
    except:
        message = "Owner mail id is invalid"

    return view_stationvehicle(request)



