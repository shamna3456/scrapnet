from django.conf.urls import url
from temp import views

urlpatterns = [
    url('temp_admin/',views.admin),
    url('temp_home/', views.home),
    url('temp_police/', views.police),
    url('temp_rto/', views.RTO),
    url('temp_scrap/', views.scrapdealer),
    url('temp_user/', views.user),
]