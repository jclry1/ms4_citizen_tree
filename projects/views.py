# from django.views.generic.detail import DetailView
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


class ReportView(DetailView):
    model = Update
    template_name = 'projects/report.html'
    context_object_name = 'report'    