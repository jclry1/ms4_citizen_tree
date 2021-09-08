from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='projects'),
    path('updates/', views.UpdatesView.as_view(), name = 'updates'),
    path('reports/<int:pk>/', views.ReportView.as_view(), name='report'),
    path('<slug:slug>/', views.SpotlightView.as_view(), name='spotlight'),
    ]