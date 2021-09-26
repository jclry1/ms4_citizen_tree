# Setup based on Django for Professionals
# Understanding of class-based view from: https://www.youtube.com/watch?v=GxA2I-n8NR8

from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.core.mail import send_mail
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "My heading for the home page"
        if self.request.user.is_authenticated:
            user = CustomUser.objects.get(pk=self.request.user.pk)
            context ['username'] = user.username
        
        """ 
        Test sendgrid integration:
        send_mail('Subject here', 'Here is the message.', 'ms4.citizentree@gmail.com', ['jclry76@gmail.com'], fail_silently=False) """
        print('hello')

        return context

# Custom error page creation based on: https://engineertodeveloper.com/serving-custom-error-pages-with-django/

def custom_error_404(request, exception):
    return render(request, '404.html', {})


def custom_error_500(request):
    return render (request, '500.html', {})


def custom_error_403(request, exception):
    return render(request, '403.html', {})
