from django.shortcuts import render
from booking.models import Booking
from request_responce.views import user_view_responce
from request_responce.models import RequestResponce
import datetime
# Create your views here.
def view_confirmation(request):
    uid=request.session["u_id"]
    obj=Booking.objects.filter(scrapdealer_id=uid)
    context={
        'x':obj
    }
    return render(request,'booking/scrapdealer_view_confirmation.html',context)


# def post_booking(request,idd):
#     obj=RequestResponce.objects.get(request_responce_id=idd)
#     ob=Booking()
#     ob.request_response_id=idd
#     ob.user_id=obj.user_scrap_request.user_id
#     ob.vehicle_id=obj.user_scrap_request.vehicle_id
#     ob.date=datetime.datetime.today()
#     ob.time=datetime.datetime.now()
#     ob.status='pending'
#     ob.save()
#     return user_view_responce(request)

