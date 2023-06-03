from decimal import Decimal

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from orders.models import Order


def payment_process(request):
     order_id = request.session.get('order_id')
     order = get_object_or_404(Order, id=order_id)
     host = request.get_host()
     return render(request,
                   'payment/done.html',
                   {'order': order})


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')
