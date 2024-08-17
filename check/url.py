from django.conf.urls import url
from check import views

urlpatterns = [
     url('check/',views.check_vehicle),
     url('send/(?P<idd>\w+)',views.send_mail),
]