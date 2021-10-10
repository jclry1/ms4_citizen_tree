import stripe
from django.contrib.auth import get_user_model #https://learndjango.com/tutorials/django-best-practices-referencing-user-model
from django.core.mail import send_mail
from django.http.response import HttpResponse, JsonResponse
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views import View
from .models import Price, Donation, Donor

stripe.api_key = settings.STRIPE_SECRET_KEY

""" Code in this file relating to handling stripe payments and webhooks is from:
Stripe documentation eg: https://stripe.com/docs/payments/checkout/fulfill-orders
Tutorial 1: https://testdriven.io/blog/django-stripe-tutorial/
Tutorial 2: https://justdjango.com/blog/django-stripe-payments-tutorial """

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
        DOMAIN = 'https://ms4-citizen-tree.herokuapp.com/donations/'
        price = Price.objects.get(id=self.kwargs["pk"])
        #client_reference_id=request.user.id if request.user.is_authenticated else None,
        #donor = request.user.username if request.user.is_authenticated else None,
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
            client_reference_id=request.user.id if request.user.is_authenticated else None,
            #metadata={'donor': 'request.user.username if request.user.is_authenticated else None'}
            #donor = request.user.username if request.user.is_authenticated else None             
        )
        #print (client_reference_id)
        return redirect(checkout_session.url)
    
    
@csrf_exempt
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
    customer_email = session["customer_details"]["email"]
    amount = session["amount_total"]
    display_amount = "{0:.2f}".format(amount / 100)
    

    
    send_mail('Your donation', f'Thank you for your donation of {display_amount} euros to Citizen Tree.', 'ms4.citizentree@gmail.com', [customer_email], fail_silently=False)
    handle_checkout_session(session) # Based on: https://github.com/testdrivenio/django-stripe-checkout/blob/master/payments/views.py
    """
    Here:
    Add a row to a 'Received' model
    With: User, amount, date, 
    Received.objects.create(user=user, amount = display_amount, date = now,)

    do this by calling another function: handle_checkout_session(session) - see https://github.com/testdrivenio/django-stripe-checkout/blob/master/payments/views.py
    """
  return HttpResponse(status=200) 

def handle_checkout_session(session):
    # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model
    # https://learndjango.com/tutorials/django-best-practices-referencing-user-model

    User = get_user_model()
    # client_reference_id = user's id
    client_reference_id = session.get("client_reference_id")
    # payment_intent = session.get("payment_intent")

    if client_reference_id is None:
        """Customer wasn't logged in when purchasing - this shouldn't happen
        because the donate button is visible only to logged-in users - To do!""" 
        return

    # Customer was logged in we can now fetch the Django user and make changes to our models
    try:
        user = User.objects.get(id=client_reference_id)
        customer_email = session["customer_details"]["email"]
        amount = session["amount_total"]
        display_amount = "{0:.2f}".format(amount / 100)
        hi_name = user.username
        #print(user.username, "just purchased something.")
        send_mail('Thank you for your donation', f'Hi there {hi_name}, thank you for your donation of {display_amount} euros to Citizen Tree.', 
        'ms4.citizentree@gmail.com', [customer_email], fail_silently=False)

        # To Do: make changes to our models.

    except User.DoesNotExist:
        pass

