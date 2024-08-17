from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def scrapdealer_payment(request):
    obj = Payment.objects.all()
    context = {
        'x': obj
    }
    return render(request,'payment/scrapdealer_view_payment.html',context)

def user_payment(request):
    obj = Payment.objects.all()
    context = {
        'x': obj
    }
    return render(request,'payment/user_view_payment.html',context)