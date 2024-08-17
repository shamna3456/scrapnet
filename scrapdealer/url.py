from django.conf.urls import url
from scrapdealer import views

urlpatterns = [
    url('scrap_dealer/',views.manage_scrap_dealer),
    url('manage_scrap_rto/',views.rto_view),
    url('scrap_reg/',views.scrapdealer_reg),
    url('profile_update/',views.view_update),

    url('approve/(?P<idd>\w+)', views.approve),
    url('reject/(?P<idd>\w+)', views.reject),
    url('delete/(?P<idd>\w+)', views.delete)
]