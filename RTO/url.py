from django.conf.urls import url
from RTO import views

urlpatterns = [
    url('edit/(?P<idd>\w+)',views.admin_edit),
    url('delete/(?P<idd>\w+)',views.delete),
    url('manage_rto/',views.manage_rto_work),
    url('rto_reg/',views.rto_register),
    url('rto_profile/',views.rto_view_profile),
]