
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='projects'),
    path('updates/', views.UpdatesView.as_view(), name = 'updates'),
    path('updates/add/<slug:slug>', views.AddUpdateView.as_view(), name='add-update'),
    path('reports/<int:pk>/', views.ReportView.as_view(), name='report'),
    path('reports/<int:pk>/delete', views.DeleteReportView.as_view(), name='report-delete'),
    path('updates/<project>/', views.ProjectUpdatesView.as_view(), name='projupdates'),
    path('userupdates/', views.UserUpdatesView.as_view(), name='userupdates'),
    path('<slug:slug>/', views.SpotlightView.as_view(), name='spotlight'),
    path('<slug:slug>/edit', views.ProjectEditView.as_view(), name='project-edit'),
    ]