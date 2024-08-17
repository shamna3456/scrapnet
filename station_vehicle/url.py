from django.conf.urls import url
from station_vehicle import views

urlpatterns = [
    url('station_vehicle/',views.station),
    url('view/',views.view_stationvehicle),
    url('send_mail/(?P<idd>\w+)',views.send_mail),
]