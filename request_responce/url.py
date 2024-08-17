from django.conf.urls import url
from request_responce import views

urlpatterns = [
  url('manage_responce/(?P<idd>\w+)',views.user_view_responce),
  url('post_resp/(?P<idd>\w+)',views.responce),
  url('scrap_view_res/',views.scrapdealer_view_responce),

  url('confirm/(?P<idd>\w+)', views.confirm),
]