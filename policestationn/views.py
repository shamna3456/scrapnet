from django.shortcuts import render
from policestationn.models import PoliceStation
from login.models import Login
# Create your views here.
def admin_edit_police(request,idd):
    ob=PoliceStation.objects.get(police_station_id=idd)
    context={
        "x":ob
    }
    if request.method=='POST':
        ob=PoliceStation.objects.get(police_station_id=idd)
        ob.name=request.POST.get('name')
        ob.place=request.POST.get('place')
        ob.address=request.POST.get('address')
        ob.phone=request.POST.get('phone')
        ob.email=request.POST.get('mail')
        ob.save()


        return police_station_manage(request)

    return render(request,'policestationn/admin_edit_police.html',context)

def delete(request,idd):
    ob=PoliceStation.objects.get(police_station_id=idd)
    ob.delete()
    return police_station_manage(request)

def police_station_manage(request):
    obj = PoliceStation.objects.all()
    context = {
        'x': obj
    }

    return render(request,'policestationn/manage_police.html',context)

def police_station_register(request):

    if request.method=='POST':
        uname = request.POST.get('Uname')
        if Login.objects.filter(username=uname).exists():
            message = "username already exist"
            context = {
                'msg': message
            }
            return render(request, 'policestationn/policestation_reg.html',context)
        else:
            ob=PoliceStation()
            ob.name=request.POST.get('name')
            ob.username=request.POST.get('Uname')
            ob.place=request.POST.get('place')
            ob.phone=request.POST.get('phone')
            ob.address=request.POST.get('ad')
            ob.email=request.POST.get('mail')
            ob.password=request.POST.get('pwd')
            ob.save()

            obj = Login()
            obj.username = ob.username
            obj.password=ob.password
            obj.u_id=ob.police_station_id
            obj.type='police'
            obj.save()

            message = "Registration Successful"
            context = {
                'msg': message
            }
            return render(request, 'temp/admin.html', context)

    return render(request,'policestationn/policestation_reg.html')