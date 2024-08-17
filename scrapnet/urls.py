"""scrapnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from temp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('booking/',include('booking.url')),
    url('certificate/',include('certificate.url')),
    url('login/',include('login.url')),
    url('payment/',include('payment.url')),
    url('policestationn/',include('policestationn.url')),
    url('request_responce/',include('request_responce.url')),
    url('RTO/',include('RTO.url')),
    url('scrapdealer/',include('scrapdealer.url')),
    url('scrapdealer_request/',include('scrapdealer_request.url')),
    url('scrapped_vehicle/',include('scrapped_vehicle.url')),
    url('suspicious_activity/',include('suspicious_activity.url')),
    url('user/',include('user.url')),
    url('user_scrap_request/',include('user_scrap_request.url')),
    url('vehicle/',include('vehicle.url')),
    url('temp/',include('temp.url')),
    url('check/',include('check.url')),
    url('paymentrazor/',include('paymentrazor.urls')),
    url('$', views.home),
    url('station_vehicle/',include('station_vehicle.url')),

]
