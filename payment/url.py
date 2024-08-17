from django.conf.urls import url
from payment import views

urlpatterns = [
    url('manage_scrapdealer_payment/',views.scrapdealer_payment),
    url('manage_user_payment/',views.user_payment),
]