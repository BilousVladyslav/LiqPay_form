from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from payment.views import PayView, PayCallbackView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^pay/$', PayView.as_view(), name='pay_view'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback')
]
