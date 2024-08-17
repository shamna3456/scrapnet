from django.conf.urls import url
from suspicious_activity import views

urlpatterns = [
    url('edit/(?P<idd>\w+)', views.edit_suspicious),
    url('delete/(?P<idd>\w+)',views.delete),
    url('manage_police_suspicious/', views.manage_suspicious_activity),
    url('add_activities/',views.police_suspicious_activity),
    url('scrap_suspicious/(?P<idd>\w+)', views.scrapdealer_suspicious),

]