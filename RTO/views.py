from django.shortcuts import render
from RTO.models import Rto
from login.models import Login
# Create your views here.
def admin_edit(request,idd):
    ob=Rto.objects.get(rto_id=idd)
    context={
        "x":ob
    }
    if request.method=="POST":
        ob= Rto.objects.get(rto_id=idd)
        ob.name=request.POST.get('name')
        ob.gender=request.POST.get('gender')
        ob.place=request.POST.get('place')
        ob.phone=request.POST.get('phone')
        ob.email=request.POST.get('mail')
        ob.rto_office_name=request.POST.get('offname')
        ob.save()


        return manage_rto_work(request)
    return render(request,'RTO/admin_edit_rto.html',context)

def delete(request,idd):
    obj=Rto.objects.get(rto_id=idd)
    print(obj)
    obj.delete()
    return manage_rto_work(request)

def manage_rto_work(request):
    obj = Rto.objects.all()
    context = {
        'x': obj
    }
    return render(request,'RTO/manage_rto.html',context)

def rto_register(request):
    if request.method=="POST":
        uname = request.POST.get('Uname')
        if Login.objects.filter(username=uname).exists():
            message = "username already exist"
            context = {
                'msg': message
            }
            return render(request, 'RTO/rto_reg.html',context)
        else:
            ob = Rto()
            ob.username=request.POST.get('Uname')
            ob.name=request.POST.get('name')
            ob.gender=request.POST.get('gender')
            ob.place=request.POST.get('place')
            ob.phone=request.POST.get('phone')
            ob.email=request.POST.get('mail')
            ob.rto_office_name=request.POST.get('offname')
            ob.password=request.POST.get('pwd')
            ob.save()

            obj = Login()
            obj.username = ob.username
            obj.password = ob.password
            obj.u_id = ob.rto_id
            obj.type = 'rto'
            obj.save()

            message = "Registration Successfull"
            context = {
                'msg': message
            }
            return render(request, 'temp/admin.html', context)

    return render(request,'RTO/rto_reg.html')

def rto_view_profile(request):
    uid=request.session["u_id"]
    ob=Rto.objects.get(rto_id=uid)
    context={
        "x":ob
    }
    if request.method=="POST":
        ob.name=request.POST.get('name')
        ob.gender=request.POST.get('gender')
        ob.place=request.POST.get('place')
        ob.phone=request.POST.get('phone')
        ob.email=request.POST.get('email')
        ob.rto_office_name=request.POST.get('offname')
        ob.save()
        message = "Updated"
        context = {
            'msg': message
        }
        return render(request, 'temp/rto.html', context)


    return render(request,'RTO/RTO_view_profile.html',context)

