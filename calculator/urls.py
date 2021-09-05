from django.urls import path, include
from calculator import views
from .views import calc
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'faqs', views.FaqViewSet)

urlpatterns = [
    path('', views.calc, name='calc'),
    path('faq/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', 
    namespace='rest_framework')),
]