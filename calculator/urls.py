from django.urls import path
from calculator import views
from .views import calc

urlpatterns = [
    path('', views.calc, name='calc'),
]