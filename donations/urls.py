from django.urls import path
from . import views


app_name = 'donations'

urlpatterns = [
    path('', views.DonateInfo, name="donateinfo"),
    #path('donate/',views.donate, name = "donate"),
    #path('success/<str:args>', views.successMsg, name = "success"),
]