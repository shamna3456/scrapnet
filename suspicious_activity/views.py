from django.shortcuts import render
from suspicious_activity.models import SuspiciousActivity
from user_scrap_request.models import UserScrapRequest
import requests
# Create your views here.
def manage_suspicious_activity(request):
    obj = SuspiciousActivity.objects.all()
    context = {
        'x': obj
    }
    return render(request,'suspicious_activity/manage_suspicious_activity.html',context)

def edit_suspicious(request,idd):
    ob=SuspiciousActivity.objects.get(suspicious_activity_id=idd)
    context={
        "x":ob
    }
    if request.method == 'POST':
        ob.case_no=request.POST.get('num')
        ob.case_details=request.POST.get('details')
        ob.case_date=request.POST.get('date')

        ob.save()

        return manage_suspicious_activity(request)
    return render(request,'suspicious_activity/police_edit_suspicious.html',context)

def delete(request,idd):
    ob=SuspiciousActivity.objects.get(suspicious_activity_id=idd)
    ob.delete()
    return manage_suspicious_activity(request)



from vehicle.models import Vehicle
def police_suspicious_activity(request):
    uid=request.session["u_id"]
    obj=Vehicle.objects.all()
    context={
        'x':obj
    }
    if request.method == 'POST':
        ob = SuspiciousActivity()
        ob.case_no = request.POST.get('num')
        ob.case_details = request.POST.get('details')
        ob.case_date = request.POST.get('date')
        ob.police_station_id=uid
        ob.vehicle_id=request.POST.get('v')

        ob.save()
        message = "Added"
        context = {
            'msg': message
        }
        return render(request, 'temp/police.html', context)
        return render(request,'temp/police.html')

    return render(request,'suspicious_activity/police_suspicious_activity.html',context)

def scrapdealer_suspicious(request,idd):
    ob=UserScrapRequest.objects.get(user_scrap_request_id=idd)
    obj = SuspiciousActivity.objects.filter(vehicle_id=ob.vehicle_id)
    context = {
        'x': obj
    }
    return render(request,'suspicious_activity/scrapdealer_suspicious_activity.html',context)



#
# url = "https://www.fast2sms.com/dev/bulkV2"
#
# payload = "message=hello world &language=english&route=q&numbers=8075298302"
# headers = {
#     'authorization': "key here",
#     'Content-Type': "application/x-www-form-urlencoded",
#     'Cache-Control': "no-cache",
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)