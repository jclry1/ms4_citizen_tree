import stripe
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views import View
from .models import Price, Donation


stripe.api_key = settings.STRIPE_SECRET_KEY



class DonateLandingPage(TemplateView):            
    template_name = "donations/donate.html"

    def get_context_data(self, **kwargs):
        donation = Donation.objects.get(name="Regular")
        prices = Price.objects.filter(donation=donation)
        context = super(DonateLandingPage,
                        self).get_context_data(**kwargs)
        context.update({
            "donation": donation,
            "prices": prices
        })
        return context


class SuccessView(TemplateView):
    template_name = "donations/success.html"


class CancelView(TemplateView):
    template_name = "donations/cancel.html"


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        DOMAIN = 'http://127.0.0.1:8000/donations/'
        price = Price.objects.get(id=self.kwargs["pk"])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= DOMAIN + 'success/',
            cancel_url= DOMAIN + 'cancel/',
        )
        return redirect(checkout_session.url)
    
    """ checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': 'price_1JYnvKGXFBy9KvEyU8nAhWTf',
                'quantity': 1,
            },
        ],
        payment_method_types=[
            'card',
        ],
        metadata={
            "placeholder":"placeholder data"
        },
        mode='payment',
        success_url= DOMAIN + 'success/',
        cancel_url= DOMAIN + 'cancel/',
    )
    return redirect(checkout_session.url, code=303) """

# From: https://stripe.com/docs/payments/checkout/fulfill-orders

""" @csrf_exempt
def stripe_webhook(request):
  payload = request.body

  # For now, you only need to print out the webhook payload so you can see
  # the structure.
  print(payload)

  return HttpResponse(status=200) """


  
# Below based on https://testdriven.io/blog/django-stripe-tutorial/ and https://www.youtube.com/watch?v=722A27IoQnk
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        session = event['data']['object']
        print(session)

        #send_mail('Donation to Citizen Tree', session, 'ms4.citizentree@gmail.com', customer_email, fail_silently=False)
        """ send_mail(
            subject="Thanks for your donation",
            message=f"Thanks for your donation of xxx",
            recipient_list=[customer_email],
            from_email="admin@citizentree.com"
        ) """

    return HttpResponse(status=200)

""" @csrf_exempt
def stripe_webhook(request):
  endpoint_secret = settings.STRIPE_WH_SECRET
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    print(session)

  # Passed signature verification
  return HttpResponse(status=200) """



""" def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
          payload, sig_header, endpoint_secret
        )
    except ValueError as e:
      # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
      # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        #product_info = session["metadata"]["placeholder"]

        print(session["customer_details"])

        send_mail(
            subject="Thanks for your donation",
            message=f"Thanks for your donation of xxx",
            recipient_list=[customer_email],
            from_email="admin@citizentree.com"
        )
    return HttpResponse(status=200) """