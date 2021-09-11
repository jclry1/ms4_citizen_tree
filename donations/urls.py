from django.urls import path
from . import views


app_name = 'donations'

urlpatterns = [
    path('', views.DonateLandingPage.as_view(), name="donate-landing"),
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session')
    #path('donate/',views.donate, name = "donate"),
    #path('success/<str:args>', views.successMsg, name = "success"),
]