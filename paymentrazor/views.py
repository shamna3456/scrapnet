from django.shortcuts import render

# Create your views here.
# rzp_test_Ey8ivDWGODPlAZ == api
# ttmCr5Cy7mQYI2Eck7W6UD3u == sec


from django.shortcuts import render
from booking.models import Booking
from payment.models import Payment
from django.conf import settings
import razorpay
from scrapped_vehicle.models import ScrappedVehicle
def payment_form(request,idd):
    uid=request.session["u_id"]
    razorpay_key = 'rzp_test_Ey8ivDWGODPlAZ'
    ob=ScrappedVehicle.objects.get(scrapped_vehicle_id=idd)
    amount=float(ob.booking.request_response.price)*100
    context={
        'razorpay_key': razorpay_key,
        'amt':str(amount)
    }
    obj=Payment()
    obj.scrapped_vehicle_id=idd
    obj.user_id=ob.booking.user_id
    obj.status='pending'
    obj.amount=ob.booking.request_response.price
    obj.ifsc=' '
    obj.account_number=' '
    obj.scrapdealer_id=uid
    obj.save()
    request.session['payid']=str(obj.payment_id)
    return render(request, 'paymentrazor.html', context)

from django.http import JsonResponse
from scrapdealer_request.models import ScrapdealerRequest
def update_payment(request):
    uid = request.session["u_id"]
    ob=Payment.objects.get(payment_id=request.session['payid'])
    ob.status='paid'
    ob.save()
    obj = ScrappedVehicle.objects.get(scrapped_vehicle_id=ob.scrapped_vehicle_id)
    obj.status='paid'
    obj.save()
    # msg = {
    #
    #     'al': 'Payment completed Successfully',
    #
    # }
    # return JsonResponse(msg)
    message="Successfully Paid"
    obj = Booking.objects.filter(scrapdealer_id=uid)
    context = {
        'x': obj,
        'msg': message
    }
    return render(request, 'booking/scrapdealer_view_confirmation.html', context)