# Setup based on Django for Professionals
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home/index.html'