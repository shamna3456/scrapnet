from django.shortcuts import render
from scrapped_vehicle.models import ScrappedVehicle
from booking.models import Booking
# Create your views here.
def police_view_vehicle(request):
    obj = ScrappedVehicle.objects.all()
    context = {
        'x': obj
    }
    return render(request,'scrapped_vehicle/police_view_scrapped_vehicle.html',context)

def rto_view_vehicle(request):
    obj = ScrappedVehicle.objects.all()
    context = {
        'x': obj
    }
    return render(request,'scrapped_vehicle/RTO_scrapped_Vehicle.html',context)

def scrapdealer_view_vehicle(request):
    uid=request.session["u_id"]
    obj = ScrappedVehicle.objects.filter(booking__scrapdealer_id=uid)
    context = {
        'x': obj
    }
    return render(request,'scrapped_vehicle/user_scrapped_vehicle_status.html',context)

def user_view_scrapped_vehicle(request):
    uid=request.session["u_id"]
    obj = ScrappedVehicle.objects.filter(booking__user_id=uid)
    context = {
        'x': obj
    }
    return render(request, 'scrapped_vehicle/user_view_scrapped_vehicle.html', context)

from django.http import HttpResponseRedirect
def send_status(request,idd):
    uid=request.session["u_id"]
    if ScrappedVehicle.objects.filter(booking_id=idd).exists():
        message="Already send status"
    else:
        ob=ScrappedVehicle()
        ob.booking_id=idd
        ob.status='Completed'
        ob.save()
        # message="Successfully sended"
        return HttpResponseRedirect('/paymentrazor/payment-form/'+str(ob.scrapped_vehicle_id))
    obj = Booking.objects.filter(scrapdealer_id=uid)
    context = {
        'x': obj,
        'msg':message
    }
    return render(request, 'booking/scrapdealer_view_confirmation.html', context)

def scrapdealer_view_vehicle(request):
    obj = ScrappedVehicle.objects.all()
    context = {
        'x': obj
    }
    return render(request,'scrapped_vehicle/scrapdealer_view_scrapped_vehicle.html',context)

def admin_view_vehicle(request):
    obj = ScrappedVehicle.objects.all()
    context = {
        'x': obj
    }
    return render(request,'scrapped_vehicle/admin_view_scrapped.html',context)