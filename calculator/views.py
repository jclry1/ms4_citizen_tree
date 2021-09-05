from django.shortcuts import render
from .models import faq
from django.http import HttpResponse 
from rest_framework import viewsets
from .serializers import faqSerializer

def calc(request):
    return render(request, 'calculator/calculate.html')

class FaqViewSet(viewsets.ReadOnlyModelViewSet): # Read only means user cannot post a new object: https://www.django-rest-framework.org/api-guide/viewsets/#readonlymodelviewset
    queryset = faq.objects.all()
    serializer_class = faqSerializer
