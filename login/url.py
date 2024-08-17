from django.conf.urls import url
from login import views

urlpatterns = [
     url('manage_login/',views.login_page),
]