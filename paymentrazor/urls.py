# payment/urls.py
from django.urls import path
from .views import payment_form
from paymentrazor import views
from django.conf.urls import url


urlpatterns = [
    url('payment-form/(?P<idd>\w+)',payment_form),
    url('post_pay/',views.update_payment),
]
