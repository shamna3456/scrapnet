from django.shortcuts import render
from check.models import Check
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.
def check_vehicle(request):
    if request.method == "POST":
        vno=request.POST.get('vno')
        ob=Check.objects.filter(vehicle_no__contains=vno)
        if len(ob)>0:
            obj=Check.objects.filter(vehicle_no__contains=vno)

            cdt = timezone.now()
            cdate = cdt.date()

            edate=obj[0].vehicle_expiry
            scount=int(obj[0].suspicious_count)

            if cdate>edate or scount>=4:
                message="Vehicle Expired.Mail send to vehicle owner"
                context={
                    'y':1,
                    'x':obj[0]
                }
                return render(request, 'check/result.html',context)
            else:
                context={
                    'x':obj[0]
                }
                return render(request, 'check/result.html',context)
    return render(request,'check/police_check_vehicle.html')

import smtplib
def send_mail(request,idd):
    ob=Check.objects.get(check_id=idd)
    email = "projectmailbg@gmail.com"
    cdt = timezone.now()
    cdate = cdt.date()

    edate = ob.vehicle_expiry
    scount = int(ob.suspicious_count)

    if cdate>edate:
        msg = "Your Vehicle Vehicle No: " + ob.vehicle_no + ' has Expired.: '
    elif scount>=4:
        msg = "Your Vehicle Vehicle No: " + ob.vehicle_no + ' had more than four suspicious activities.: '
    else:
        msg = "Your Vehicle Vehicle No: " + ob.vehicle_no + ' has Expired and have more than four suspicious activities. '
    try:
        em=ob.email
        sub = "Warning. Vehicle Expiry"
        text = f'subject : {sub} \n\n{msg}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, 'iqjjrhsyerovorav')
        server.sendmail(email, str(em), text)
        message="send"
        # return HttpResponseRedirect('/check/check/')
    except:
        message = "Owner mail id is invalid"
    context = {
        'y': 1,
        'x': ob,
        'msg': message,
    }
    return render(request,'check/result.html',context)
