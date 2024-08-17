from django.conf.urls import url
from user_scrap_request import views

urlpatterns = [
    url('manage_scrapdealer_view_request/', views.scrapdealer_view_user),
    url('post_screp/(?P<idd>\w+)', views.user_scrap),
    url('user_view_request/', views.user_view_details),
]