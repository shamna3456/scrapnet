from django.conf.urls import url
from scrapped_vehicle import views

urlpatterns = [
    url('manage_police_vehicle/', views.police_view_vehicle),
    url('manage_rto_view_vehicle/', views.rto_view_vehicle),
    url('user/', views.user_view_scrapped_vehicle),
    url('scrapped_vehicle_view/', views.scrapdealer_view_vehicle),
    url('send/(?P<idd>\w+)',views.send_status),
    url('scrap_dealer_view_vehicle/',views.scrapdealer_view_vehicle),
    url('admin_view_vehicle/', views.admin_view_vehicle),
]