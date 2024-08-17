from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
from scrapdealer.models import Scrapdealer
# Create your views here.
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        pswd=request.POST.get("pwd")
        obj= Login.objects.filter(username=username,password=pswd)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/temp_admin/')
            elif tp=="police":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/temp_police/')
            elif tp=="user":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/temp_user/')
            elif tp=="rto":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/temp_rto/')
            elif tp=="scrap_dealer":
                uob=Scrapdealer.objects.get(scrapdealer_id=uid)
                if uob.status=='approved':
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/temp_scrap/')
                else:
                    objlist = "Your registration is pending ....!"
                    context = {
                        'msg': objlist,
                    }
                return render(request, 'login/login.html', context)
        else:
            objlist="username or Password incorrect,Please try again ....!"
            context={
                'msg':objlist,
            }
        return render(request,'login/login.html',context)
    return render(request, 'login/login.html')
