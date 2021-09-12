import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View


stripe.api_key = settings.STRIPE_SECRET_KEY


class DonateLandingPage(TemplateView):              # This works
    template_name = "donations/donate.html"


class SuccessView(TemplateView):
    template_name = "donations/success.html"


class CancelView(TemplateView):
    template_name = "donations/cancel.html"


def create_checkout_session(request):
    DOMAIN = 'http://127.0.0.1:8000/donations/'
    
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': 'price_1JYnvKGXFBy9KvEyU8nAhWTf',
                'quantity': 1,
            },
        ],
        payment_method_types=[
            'card',
        ],
        mode='payment',
        success_url= DOMAIN + 'success/',
        cancel_url= DOMAIN + 'cancel/',
    )
    return redirect(checkout_session.url, code=303)