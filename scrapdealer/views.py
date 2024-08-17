from django.shortcuts import render
from scrapdealer.models import Scrapdealer
from django.core.files.storage import FileSystemStorage
from login.models import Login
# Create your views here.
def manage_scrap_dealer(request):
    obj = Scrapdealer.objects.all()
    context = {
        'x': obj
    }
    return render(request,'scrapdealer/manage_scrapdealer.html',context)


def approve(request,idd):
    ob=Scrapdealer.objects.get(scrapdealer_id=idd)
    ob.status='approved'
    ob.save()
    return manage_scrap_dealer(request)

def reject(request,idd):
    ob=Scrapdealer.objects.get(scrapdealer_id=idd)
    ob.status='rejected'
    ob.save()
    return manage_scrap_dealer(request)

def delete(request,idd):
    ob=Scrapdealer.objects.get(scrapdealer_id=idd)
    ob.delete()
    return manage_scrap_dealer(request)



def rto_view(request):
    obj = Scrapdealer.objects.all()
    context = {
        'x': obj
    }
    return render(request,'scrapdealer/RTO_view_scrapdealer.html',context)


def scrapdealer_reg(request):
    if request.method=='POST':
        uname=request.POST.get('Uname')
        pwd=request.POST.get('pwd')
        cpwd=request.POST.get('cpwd')
        if Login.objects.filter(username=uname).exists():
            message="username already exist"
            context={
                'msg':message
            }
            return render(request, 'scrapdealer/scrapdealer_reg.html',context)
        elif pwd==cpwd:
            ob=Scrapdealer()
            ob.name=request.POST.get('name')

            myfile = request.FILES['licence']
            fs = FileSystemStorage()
            file_name = fs.save(myfile.name, myfile)
            ob.lisence = myfile.name

            ob.place=request.POST.get('place')
            ob.phone=request.POST.get('phone')
            ob.email=request.POST.get('mail')
            ob.username=request.POST.get('Uname')
            ob.password=request.POST.get('pwd')
            ob.start_time=request.POST.get('stime')
            ob.end_time=request.POST.get('etime')
            ob.service_provided=request.POST.get('service')
            ob.status='pending'
            ob.save()

            obj = Login()
            obj.username = ob.name
            obj.password = ob.password
            obj.u_id = ob.scrapdealer_id
            obj.type = 'scrap_dealer'
            obj.save()

            message = "Registration success full"
            context = {
                'msg': message
            }
            return render(request, 'temp/home.html', context)

        else:
            message = "Password Miss match"
            context = {
                'msg': message
            }
            return render(request, 'scrapdealer/scrapdealer_reg.html', context)
    return render(request,'scrapdealer/scrapdealer_reg.html')

def view_update(request):
    uid=request.session["u_id"]
    ob=Scrapdealer.objects.get(scrapdealer_id=uid)
    print(ob)
    if request.method == 'POST':
        ob.name = request.POST.get('name')
        ob.place = request.POST.get('place')
        ob.phone = request.POST.get('phone')
        ob.email = request.POST.get('mail')
        # ob.username = request.POST.get('Uname')
        # ob.password = request.POST.get('pwd')
        ob.start_time = request.POST.get('stime')
        ob.end_time = request.POST.get('etime')
        ob.service_provided = request.POST.get('service')
        myfile = request.FILES['licence']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.lisence = myfile.name
        ob.save()
        # return view_update(request)
        message="Successfully updated"
        context={
            'msg':message
        }
        return render(request,'temp/scrapdealer.html',context)
    context = {
        'x': ob
    }
    return render(request,'scrapdealer/scrapdealer_view&update.html',context)
