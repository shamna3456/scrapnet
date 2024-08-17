from django.conf.urls import url
from user import views

urlpatterns = [
    url('manage_user_rto/',views.rto_user),
    url('user_reg/', views.user_register),
    url('manage_user_update/', views.user_view_update),
]