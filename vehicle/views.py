from django.shortcuts import render
from vehicle.models import Vehicle
from django.core.files.storage import FileSystemStorage
from scrapnet import settings
from pandas import read_excel
from sklearn.tree import DecisionTreeClassifier

# Create your views here.
def rto_vehicle(request):
    obj =Vehicle.objects.all()
    context = {
        'x': obj
    }
    return render(request,'vehicle/RTO_manage_vehicle.html',context)

def approve(request,idd):
    ob=Vehicle.objects.get(vehicle_id=idd)
    ob.status='approved'
    ob.save()
    return rto_vehicle(request)

def reject(request,idd):
    ob=Vehicle.objects.get(vehicle_id=idd)
    ob.status='rejected'
    ob.save()
    return rto_vehicle(request)

from django.utils import timezone
def rto_view_expiry(request):
    cdt=timezone.now()
    cdate=cdt.date()
    obj = Vehicle.objects.filter(expiry_date__lt=cdate)
    context = {
        'x': obj
    }
    return render(request,'vehicle/RTO_view_expired_vehicle.html',context)


def user_edit_vehicle(request,idd):
    ob=Vehicle.objects.get(vehicle_id=idd)
    context={
        'x' :ob
    }
    if request.method=="POST":
        ob.vehicle_name=request.POST.get('name')
        ob.vehicle_number=request.POST.get('num')
        ob.colour=request.POST.get('clr')
        ob.model=request.POST.get('model')
        ob.owner_name=request.POST.get('ownernum')
        ob.owner_contact=request.POST.get('ownercon')
        ob.insurance_details=request.POST.get('insurence')
        ob.registration_date=request.POST.get('reg')
        ob.last_service_date=request.POST.get('sdate')
        ob.mileage=request.POST.get('mileage')

        myfile = request.FILES['ee']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.pollution_certificate = myfile.name

        ob.engine_number = request.POST.get('engine')

        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        file_name = fs.save(myfile.name,myfile)
        ob.photo=myfile.name

        ob.expiry_date=request.POST.get('expiry')
        ob.vehicle_type=request.POST.get('type')
        ob.save()
        message = "Update"
        context = {
            'msg': message
        }
        # return render(request, 'temp/user.html', context)
        return user_view_expiry(request)
    return render(request,'vehicle/user_edit_vehicle.html',context)


def delete(request,idd):
    ob=Vehicle.objects.get(vehicle_id=idd)
    ob.delete()
    message = "Deleted"
    context = {
        'msg': message
    }
    return user_view_expiry(request)
    # return render(request, 'temp/user.html', context)
    # return update_delete_vehicle(request)


def update_delete_vehicle(request):
    uid=request.session["u_id"]
    obj = Vehicle.objects.filter(user_id=uid)
    context = {
        'x': obj
    }

    return render(request,'vehicle/user_update&delete_vehicle.html',context)



def vehicle_register(request):
    uid=request.session["u_id"]
    if request.method=="POST":
        ob=Vehicle()
        ob.vehicle_name=request.POST.get('name')
        ob.vehicle_number=request.POST.get('num')
        ob.colour=request.POST.get('clr')
        ob.model=request.POST.get('model')
        ob.owner_name=request.POST.get('ownernum')
        ob.owner_contact=request.POST.get('ownercon')

        ob.insurance_details=request.POST.get('insurence')
        ob.registration_date=request.POST.get('reg')
        ob.last_service_date=request.POST.get('date')
        ob.mileage=request.POST.get('mileage')

        myfile=request.FILES['certi']
        fs = FileSystemStorage()
        file_name=fs.save(myfile.name,myfile)
        ob.pollution_certificate=myfile.name

        ob.engine_number=request.POST.get('engine')

        myfile = request.FILES['photo']
        fs = FileSystemStorage()
        file_name = fs.save(myfile.name, myfile)
        ob.photo = myfile.name

        ob.user_id=uid
        ob.expiry_date=request.POST.get('expiry')
        ob.status='pending'

        ob.vehicle_type=request.POST.get('type')
        ob.save()

        message = "Registration success full"
        context = {
            'msg': message
        }
        return user_view_expiry(request)
        # return render(request, 'temp/user.html', context)
    return render(request,'vehicle/user_vehicle_reg.html')


def user_view_expiry(request):
    uid=request.session["u_id"]
    cdt = timezone.now()
    cdate = cdt.date()
    # obj = Vehicle.objects.filter(expiry_date__lt=cdate,user_id=uid)
    obj = Vehicle.objects.filter(user_id=uid)
    # obj = Vehicle.objects.all()
    context = {
        'x': obj
    }
    return render(request,'vehicle/User_view_expired_vehicle.html',context)



def predict(request):
    if request.method=="POST":
        print("start")
        a1 = request.POST.get('q1')
        print(a1)
        a2 = request.POST.get('q2')
        print(a2)
        a3 = request.POST.get('q3')
        print(a3)
        a4 = request.POST.get('q4')
        print(a4)
        a5 = request.POST.get('q5')
        print(a5)
        a6 = request.POST.get('q6')
        print(a6)
        a7 = request.POST.get('q7')
        print(a7)
        a8 = request.POST.get('q8')
        print(a8)
        a9 = request.POST.get('q9')
        print(a9)
        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "scrap.xlsx"
        data = read_excel(imgpath, "Sheet1")
        X = data.iloc[:, 0:9].values
        y = data.iloc[:, 9].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        # test = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11),int(a12),
        #         int(a13),int(a14),int(a15),int(a16),int(a17),int(a18),int(a19),int(a20),int(a21),int(a22),int(a23),int(a24),
        #         int(a25),int(a26),int(a27),int(a28),int(a29),int(a30),int(a31),int(a32),int(a33),int(a34),int(a35),int(a36),
        #         int(a37),int(a38),int(a39),int(a40),int(a41)]

        test = [int(a1), int(a2), int(a3), int(a4), int(a5), int(a6),int(a7), int(a8), int(a9),]
        y_pred = dtc.predict([test])
        print(y_pred)
        k=str(y_pred[0])
        print(k)
        context = {
            'res':k,
        }

        return render(request, 'vehicle/result.html', context)
    return render(request, 'vehicle/predict.html',)

def vehicle_details(request,idd):
    ob = Vehicle.objects.get(vehicle_id=idd)
    context = {
        'i': ob
    }

    return render(request, 'vehicle/vehicle_details.html', context)

def scrap_predict(request):
    if request.method=="POST":
        print("start")
        a1 = request.POST.get('q1')
        print(a1)
        a2 = request.POST.get('q2')
        print(a2)
        a3 = request.POST.get('q3')
        print(a3)
        a4 = request.POST.get('q4')
        print(a4)
        a5 = request.POST.get('q5')
        print(a5)
        a6 = request.POST.get('q6')
        print(a6)
        a7 = request.POST.get('q7')
        print(a7)
        a8 = request.POST.get('q8')
        print(a8)
        a9 = request.POST.get('q9')
        print(a9)
        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "scrap.xlsx"
        data = read_excel(imgpath, "Sheet1")
        X = data.iloc[:, 0:9].values
        y = data.iloc[:, 9].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        # test = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11),int(a12),
        #         int(a13),int(a14),int(a15),int(a16),int(a17),int(a18),int(a19),int(a20),int(a21),int(a22),int(a23),int(a24),
        #         int(a25),int(a26),int(a27),int(a28),int(a29),int(a30),int(a31),int(a32),int(a33),int(a34),int(a35),int(a36),
        #         int(a37),int(a38),int(a39),int(a40),int(a41)]

        test = [int(a1), int(a2), int(a3), int(a4), int(a5), int(a6),int(a7), int(a8), int(a9),]
        y_pred = dtc.predict([test])
        print(y_pred)
        k=str(y_pred[0])
        print(k)
        context = {
            'res':k,
        }

        return render(request, 'vehicle/scrap_result.html', context)
    return render(request, 'vehicle/scrap_predict.html',)
