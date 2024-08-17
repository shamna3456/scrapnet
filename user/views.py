from django.shortcuts import render
from user.models import User
from login.models import Login
# Create your views here.
def rto_user(request):
    obj = User.objects.all()
    context = {
        'x': obj
    }
    return render(request,'user/RTO_view_user.html',context)

def user_register(request):
    if request.method=="POST":
        uname = request.POST.get('Uname')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        if Login.objects.filter(username=uname).exists():
            message = "username already exist"
            context = {
                'msg': message
            }
            return render(request, 'user/user_reg.html',context)
        elif pwd == cpwd:
            ob=User()
            ob.username=request.POST.get('Uname')
            ob.name=request.POST.get('name')
            ob.place=request.POST.get('place')
            ob.address=request.POST.get('address')
            ob.phone_number = request.POST.get('phone')
            ob.gender = request.POST.get('gender')
            ob.email_id=request.POST.get('mail')
            ob.password = request.POST.get('pwd')
            # ob.Confirm_Password = request.POST.get('cpwd')
            ob.save()

            obj = Login()
            obj.username = ob.username
            obj.password = ob.password
            obj.u_id = ob.user_id
            obj.type = 'user'
            obj.save()
            message = "Registration success full"
            context = {
                'msg': message
            }
            return render(request,'temp/home.html',context)
        else:
            message = "Password Miss match"
            context = {
                'msg': message
            }
            return render(request, 'user/user_reg.html', context)
    return render(request,'user/user_reg.html')

def user_view_update(request):
    uid=request.session["u_id"]
    ob=User.objects.get(user_id=uid)
    context={
        'x':ob
    }
    if request.method == "POST":
        ob.name=request.POST.get('name')
        ob.place = request.POST.get('place')
        ob.address = request.POST.get('address')
        ob.phone_number = request.POST.get('phone')
        ob.gender = request.POST.get('gender')
        ob.email_id = request.POST.get('email')
        ob.save()
        context={
            'x':ob
        }
        message = "Updated"
        context = {
            'msg': message
        }
        return render(request, 'temp/user.html', context)
    return render(request,'user/user_view&update_profile.html',context)

