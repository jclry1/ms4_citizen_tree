# Setup based on Django for Professionals
# Understanding of class-based view from: https://www.youtube.com/watch?v=GxA2I-n8NR8

from django.views.generic import TemplateView
from accounts.models import CustomUser


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "My heading for the home page"
        if self.request.user.is_authenticated:
            user = CustomUser.objects.get(pk=self.request.user.pk)
            context ['username'] = user.username
        return context