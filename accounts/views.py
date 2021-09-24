# Setup based on Django for Professionals
from allauth.account.views import SignupView # https://stackoverflow.com/questions/62039143/django-allauth-confirmation-verification-email-not-sent-after-signing-up
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.
class SignupPageView(SignupView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'