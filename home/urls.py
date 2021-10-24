# Setup basedon Django for Professionals
from django.contrib import admin
from django.urls import path
from .views import HomePageView, ContactView

app_name = 'home'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),

]