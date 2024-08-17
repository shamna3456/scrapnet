from django.conf.urls import url
from vehicle import views

urlpatterns = [
    url('manage_rto_view_vehicle/',views.rto_vehicle),
    url('manage_vehicle_expiry/',views.rto_view_expiry),
    url('edit/(?P<idd>\w+)',views.user_edit_vehicle),
    url('delete/(?P<idd>\w+)',views.delete),
    url('manage_vehicle_update/',views.update_delete_vehicle),
    url('vehicle_reg/',views.vehicle_register),
    url('manage_user_vehicle_expiry/',views.user_view_expiry),

    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)', views.reject),
    url('prediction/', views.predict),
    url('details/(?P<idd>\w+)',views.vehicle_details),
    url('scrap_dealer_predict/',views.scrap_predict),

]