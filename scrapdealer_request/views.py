from django.shortcuts import render
from scrapdealer_request.models import ScrapdealerRequest
from RTO.models import Rto
from user_scrap_request.models import UserScrapRequest
# Create your views here.
def manage(request):
    uid=request.session["u_id"]
    obj = ScrapdealerRequest.objects.filter(rto_id=uid)
    context = {
        'x': obj
    }
    return render(request,'scrapdealer_request/RTO_view_scrapdealer_request.html',context)


def approve(request,idd):
    ob=ScrapdealerRequest.objects.get(scrapdealer_request_id=idd)
    ob.status='approved'
    ob.save()
    return manage(request)

def reject(request,idd):
    ob=ScrapdealerRequest.objects.get(scrapdealer_request_id=idd)
    ob.status='rejected'
    ob.save()
    return manage(request)
def scrapdealer_forward(request,idd):
    uid=request.session["u_id"]
    obj=Rto.objects.all()
    context={
        'x':obj
    }
    if request.method=='POST':
        if ScrapdealerRequest.objects.filter(user_scrap_request_id=idd,scrapdealer_id=uid).exists():
            message="Already forwarded"

        else:
            ob=ScrapdealerRequest()
            ob.rto_id=request.POST.get('rto')
            ob.scrapdealer_id=uid
            ob.user_scrap_request_id=idd
            ob.status='pending'
            ob.save()
            message='Forwarded'

        obj = UserScrapRequest.objects.all()
        context = {
            'x': obj,
            'msg': message
        }
        return render(request, 'user_scrap_request/scrapdealer_view_user_request.html', context)
    return render(request, 'scrapdealer_request/scrapdealer_forward.html',context)




def scrap_dealer_view(request,idd):
    obj=ScrapdealerRequest.objects.filter(user_scrap_request_id=idd)
    context={
        'x':obj
    }
    return render(request,'scrapdealer_request/rto_view_req.html',context)


