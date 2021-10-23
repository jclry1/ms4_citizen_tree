# Setup based on Django for Professionals
# Understanding of class-based view from: https://www.youtube.com/watch?v=GxA2I-n8NR8

from django.db.models.aggregates import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import TemplateView
from accounts.models import CustomUser
from donations.models import Donor
from django.db.models import Sum
from shop.models import Order
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total_cent_amount = Donor.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0
        """
        Reference: 
        https://stackoverflow.com/questions/27596574/how-to-just-retrieve-the-integer-of-a-aggregate-query-in-django
        'or 0' - https://www.reddit.com/r/django/comments/fui93z/how_to_make_aggregate_return_0_instead_of_none/

        See info on Donations page or ReadMe for calculation assumptions.
        """
        total_euro_amount = total_cent_amount/100
        total_sink=total_euro_amount*1.46   #Value of total sink is kg 
        context['total_sink'] = round(total_sink)
        context['d_sink_js'] = {"donor_sink": total_sink } #Dict to pass to pie.js via json_script

        if self.request.user.is_authenticated:
            user = CustomUser.objects.get(pk=self.request.user.pk)
            context ['username'] = user.username

            donor_cent_amount = Donor.objects.filter(donor=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0
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
