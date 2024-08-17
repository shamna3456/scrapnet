from django.shortcuts import render
from  request_responce.models import RequestResponce
from user_scrap_request.models import UserScrapRequest
from booking.models import Booking
# Create your views here.
def user_view_responce(request,idd):
    obj = RequestResponce.objects.filter(user_scrap_request_id=idd)
    context = {
        'x': obj
    }
    return render(request,'request_responce/user_view_request_responce.html',context)


def responce(request,idd):
    uid=request.session["u_id"]
    if request.method=='POST':
        if RequestResponce.objects.filter(user_scrap_request_id=idd,scrapdealer_id=1).exists():
            message = "Already added"
        else:
            ob=RequestResponce()
            ob.responce_details=request.POST.get('detail')
            ob.price=request.POST.get('price')
            ob.scrapdealer_id=uid
            ob.user_scrap_request_id=idd
            ob.status='pending'
            ob.save()
            message = 'Response added'

        obj = UserScrapRequest.objects.all()
        context = {
            'x': obj,
            'msg': message
        }
        return render(request, 'user_scrap_request/scrapdealer_view_user_request.html', context)

    return  render(request,'request_responce/responce.html')


def scrapdealer_view_responce(request):
    uid=request.session["u_id"]
    obj=RequestResponce.objects.filter(scrapdealer_id=uid)
    context={
        'x':obj
    }
    return render(request,'request_responce/scrapdealer_view_res.html',context)


def confirm(request,idd):
    if RequestResponce.objects.filter(request_responce_id=idd,status='Accepted').exists():
        message="Request already confirmed"

    else:
        ob=RequestResponce.objects.get(request_responce_id=idd)
        ob.status='Accepted'
        ob.save()

        bob=Booking()
        bob.request_response_id=idd
        bob.user_id=ob.user_scrap_request.user_id
        bob.vehicle_id=ob.user_scrap_request.vehicle_id
        bob.status='Booked'
        bob.scrapdealer_id=ob.scrapdealer_id
        bob.save()

        obj=RequestResponce.objects.filter(user_scrap_request_id=ob.user_scrap_request_id).exclude(status='Accepted')
        for i in obj:
            i.status='Rejected'
            i.save()
        message = "Request confirmed"

    obj = RequestResponce.objects.filter(user_scrap_request_id=idd)
    context = {
        'x': obj,
        'msg': message
    }
    return render(request, 'request_responce/user_view_request_responce.html', context)