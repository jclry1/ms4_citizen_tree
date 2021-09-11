import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import os

stripe.api_key = settings.STRIPE_SECRET_KEY

def DonateInfo(request):
    return render(request, 'donations/donate.html')

class DonateLandingPage(TemplateView):
    template_name = "donations/donate.html"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://127.0.0.1:8000/donations/'

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
              'card',
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return JsonResponse(
            {
                'id': checkout_session.id
            }
        )    