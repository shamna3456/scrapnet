from django.conf.urls import url
from policestationn import views

urlpatterns = [
  url('edit/(?P<idd>\w+)',views.admin_edit_police),
  url('delete/(?P<idd>\w+)',views.delete),
  url('manage_police/',views.police_station_manage),
  url('police_reg/',views.police_station_register),
]