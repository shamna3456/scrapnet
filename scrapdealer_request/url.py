from django.conf.urls import url
from scrapdealer_request import views

urlpatterns = [
   url('manage_scrapdealer_request/',views.manage),
   url('post_scrap/(?P<idd>\w+)', views.scrapdealer_forward),
   url('sd_view_req/(?P<idd>\w+)',views.scrap_dealer_view),
   url('approve/(?P<idd>\w+)',views.approve),
   url('reject/(?P<idd>\w+)',views.reject),
]
