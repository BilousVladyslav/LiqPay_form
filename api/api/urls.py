from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from payment.views import PayView1, PayCallbackView, PayView2, PayView3, MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', MainPageView.as_view(), name='pay_view'),
    url(r'^product1$', PayView1.as_view(), name='pay_view'),
    url(r'^product2$', PayView2.as_view(), name='pay_view'),
    url(r'^product3$', PayView3.as_view(), name='pay_view'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback')
]
