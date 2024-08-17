from django.conf.urls import url
from booking import views


urlpatterns=[
url('manage_booking/',views.view_confirmation),
]