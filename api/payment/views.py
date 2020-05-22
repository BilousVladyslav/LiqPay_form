from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from liqpay.liqpay3 import LiqPay
from api import settings


def output_callback(callback):
    print('===========================================')
    print()
    for key, value in callback.items():
        print(f'{key}: {value}')
    print()
    print('===========================================')


class MainPageView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class PayView1(TemplateView):
    template_name = 'payment.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': '3.22',
            'currency': 'USD',
            'description': 'HONDA ACCORD LX: Low KMS car',
            'order_id': 'LowKMS-car',
            'version': '3',
            'sandbox': 0, # sandbox mode, set to 1 to enable it
            'server_url': 'https://afternoon-reaches-36943.herokuapp.com/pay-callback/', # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})


class PayView2(TemplateView):
    template_name = 'payment.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': '5.99',
            'currency': 'USD',
            'description': 'HONDA CIVIC HATCHBACK LS: Fully-Loaded car',
            'order_id' : 'FL-car',
            'version': '3',
            'sandbox': 0, # sandbox mode, set to 1 to enable it
            'server_url': 'https://afternoon-reaches-36943.herokuapp.com/pay-callback/', # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})


class PayView3(TemplateView):
    template_name = 'payment.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': '10.99',
            'currency': 'USD',
            'description': 'HONDA ACCORD HYBRID LT: Price Reduced car',
            'order_id': 'PR-car',
            'version': '3',
            'sandbox': 0, # sandbox mode, set to 1 to enable it
            'server_url': 'https://afternoon-reaches-36943.herokuapp.com/pay-callback/', # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('CALLBACK IS VALID!')
        response = liqpay.decode_data_from_str(data)
        output_callback(response)
        return HttpResponse()
