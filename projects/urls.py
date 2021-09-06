from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='projects'),
    path('<slug:slug>/', views.SingleView.as_view(), name='spotlight') ]