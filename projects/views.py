from django.views.generic.detail import DetailView
from .models import Project
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Project
    template_name = 'projects/projects.html'


class SingleView(DetailView):
    model = Project
    template_name = 'projects/projectspotlight.html'
    context_object_name = 'project'

