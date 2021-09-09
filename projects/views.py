# from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Project, Update
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Project
    template_name = 'projects/projects.html'


class SpotlightView(DetailView):
    model = Project
    template_name = 'projects/projectspotlight.html'
    context_object_name = 'project'

class UpdatesView(ListView):
    model = Update
    template_name = 'projects/updates.html'

class ProjectUpdatesView(ListView):
    template_name = 'projects/updates_by_project.html'
    
    def get_queryset(self):
        self.project = get_object_or_404(Project, title=self.kwargs['project'])
        return Update.objects.filter(project=self.project)

class ReportView(DetailView):
    model = Update
    template_name = 'projects/report.html'
    context_object_name = 'report'    