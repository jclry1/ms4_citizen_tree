# from django.views.generic.detail import DetailView
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Project, Update
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import AddUpdate, EditProject
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import LoginRequiredMixin # For class-based views (as opposed to @loginrequired)


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

class UserUpdatesView(ListView): #Credit: https://stackoverflow.com/questions/38471260/django-filtering-by-user-id-in-class-based-listview
    template_name = 'projects/updates_by_user.html'
    
    def get_queryset(self):
        return Update.objects.filter(author=self.request.user)

class ReportView(DetailView):
    model = Update
    template_name = 'projects/report.html'
    context_object_name = 'report'   


class DeleteReportView(DeleteView):
    model = Update
    template_name = 'projects/delete_update.html'
    context_object_name = 'report' 
    success_url = '../../updates'


class AddUpdateView(LoginRequiredMixin,CreateView):
    model = Update
    form_class = AddUpdate
    template_name = 'projects/add_update.html'
    success_url = '../../updates' 

    """ def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial ['title'] = 'Title for the update report'
        #initial ['slug'] = slugify(self.title) """



# https://stackoverflow.com/questions/55556165/setting-model-user-to-request-user-with-createview-in-django-returns-null-value
    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        form.instance.update_slug = slugify(form.instance.title)
        form.instance.project = Project.objects.get(slug = self.kwargs['slug'])
        return super().form_valid(form) 


class ProjectEditView(UpdateView):
    model = Project
    form_class = EditProject
    template_name = 'projects/edit_project.html'
    success_url = '../../projects'


