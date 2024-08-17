from django.shortcuts import render
from certificate.models import Certificate
from vehicle.models import Vehicle
import datetime
# Create your views here.
def rto_manage_certificate(request):
    uid=request.session["u_id"]
    obj=Certificate.objects.filter(rto_id=uid)
    context = {
        'x': obj
    }
    return render(request,'certificate/RTO_manage_certificate.html',context)

def delete (request,idd):
    ob=Certificate.objects.get(certificate_id=idd)
    ob.delete()
    return rto_manage_certificate(request)

def user_view_certificate(request):
    uid=request.session["u_id"]
    obj = Certificate.objects.filter(user_id=uid)
    context = {
        'x': obj
    }
    return render(request,'certificate/user_view_certificate.html',context)



def post_certificate(request,idd):
    obj=Vehicle.objects.get(vehicle_id=idd)
    uid=request.session["u_id"]
    # if request.method=="POST":
    if Certificate.objects.filter(vehicle_id=idd).exists():
        message="Already certified"
        obj = Vehicle.objects.all()
        context = {
            'x': obj,
            'msg': message
        }
        return render(request, 'vehicle/RTO_view_expired_vehicle.html', context)
    else:

        ob=Certificate()
        ob.rto_id=uid
        ob.holder_name = obj.owner_name
        ob.issue_date = datetime.datetime.today()
        ob.vehicle_no = obj.vehicle_number
        ob.user_id = obj.user_id
        ob.vehicle_id=idd
        if CertificateRequest.objects.filter(vehicle_id=idd).exists():
            cob=CertificateRequest.objects.get(vehicle_id=idd)
            ob.certificate_request_id = cob.certificate_request_id
        ob.save()

        message = "Success.."
        obj = Vehicle.objects.all()
        context = {
            'x': obj,
            'msg': message
        }
        return render(request, 'vehicle/RTO_view_expired_vehicle.html', context)
    # return render(request,'certificate/Add_certificate.html')



def generate_certificate(request,idd):
    ob=Certificate.objects.get(certificate_id=idd)
    context={
        'x':ob
    }
    return  render(request,'certificate/certi_page.html',context)

from scrapdealer_request.models import ScrapdealerRequest
def check(request,idd):
    ob=ScrapdealerRequest.objects.get(scrapdealer_request_id=idd)
    cno=ob.user_scrap_request.certificate_no
    obj=Certificate.objects.filter(certificate_no__contains=cno)
    context={
        'x':obj
    }
    return render(request,'certificate/Add_certificate.html',context)


from certificate.models import CertificateRequest
from RTO.models import Rto
def add_certi_req(request,idd):
    uid=request.session["u_id"]
    ob=Rto.objects.all()
    context={
        'x':ob
    }
    if request.method=="POST":
        if CertificateRequest.objects.filter(vehicle_id=idd).exists():
            message="Already requested"
        else:
            ob=CertificateRequest()
            ob.vehicle_id=idd
            ob.user_id=uid
            ob.rto_id=request.POST.get('rto')
            ob.status='pending'
            ob.save()
            message="Requested"
        obj = Vehicle.objects.filter(user_id=uid)
        # obj = Vehicle.objects.all()
        context = {
            'x': obj,
            'msg':message
        }
        return render(request, 'vehicle/User_view_expired_vehicle.html', context)

    return render(request,'certificate/add_certi_req.html',context)


def user_view(request):
    uid=request.session["u_id"]
    ob=CertificateRequest.objects.filter(user_id=uid)
    context={
        'x':ob
    }
    return render(request,'certificate/user_view_request.html',context)


def rto_view(request):
    uid=request.session["u_id"]
    ob=CertificateRequest.objects.filter(rto_id=uid)
    context={
        'x':ob
    }
    return render(request,'certificate/rto_view_request.html',context)

def post_certificate1(request,idd):
    obj=Vehicle.objects.get(vehicle_id=idd)
    uid=request.session["u_id"]
    # if request.method=="POST":
    if Certificate.objects.filter(vehicle_id=idd).exists():
        message="Already certified"
        ob = CertificateRequest.objects.filter(rto_id=uid)
        context = {
            'x': ob,
            'msg': message
        }
        return render(request, 'certificate/rto_view_request.html', context)
    else:

        ob=Certificate()
        ob.rto_id=uid
        ob.holder_name = obj.owner_name
        ob.issue_date = datetime.datetime.today()
        ob.vehicle_no = obj.vehicle_number
        ob.user_id = obj.user_id
        ob.vehicle_id=idd
        if CertificateRequest.objects.filter(vehicle_id=idd).exists():
            cob=CertificateRequest.objects.get(vehicle_id=idd)
            ob.certificate_request_id = cob.certificate_request_id
        ob.save()

        message = "Success.."
        ob = CertificateRequest.objects.filter(rto_id=uid)
        context = {
            'x': ob,
            'msg': message
        }
        return render(request, 'certificate/rto_view_request.html', context)
    # return render(request,'certificate/Add_certificate.html')