# Setup based on Django for Professionals
# Understanding of class-based view from: https://www.youtube.com/watch?v=GxA2I-n8NR8

from django.db.models.aggregates import Sum
from django.views.generic import TemplateView
from accounts.models import CustomUser
from donations.models import Donor
from django.db.models import Sum
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total_cent_amount = Donor.objects.all().aggregate(Sum('amount'))
        total_euro_amount = total_cent_amount/100
        total_sink=total_euro_amount*1.46    
        context['total_sink'] = total_sink

        if self.request.user.is_authenticated:
            user = CustomUser.objects.get(pk=self.request.user.pk)
            context ['username'] = user.username

            donor_cent_amount = Donor.objects.filter(donor=self.request.user).aggregate(Sum('amount'))
            donor_euro_amount = donor_cent_amount/100
            donor_sink = donor_euro_amount*1.46
            context['donor_sink'] = donor_sink

        return context

# Custom error page creation based on: https://engineertodeveloper.com/serving-custom-error-pages-with-django/

def custom_error_404(request, exception):
    return render(request, '404.html', {})


def custom_error_500(request):
    return render (request, '500.html', {})


def custom_error_403(request, exception):
    return render(request, '403.html', {})
