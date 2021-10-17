from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.CartView.as_view(), name='summary'),
    path('shop/', views.ProductListView.as_view(), name='product-list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name='product-spotlight'),
    path('increase-quantity/<pk>/', views.IncreaseQuantityView.as_view(), name = 'increase-qty'),
    path('decrease-quantity/<pk>/', views.DecreaseQuantityView.as_view(), name = 'decrease-qty'),
    path('remove-from-cart/<pk>/', views.RemoveFromCartView.as_view(), name = 'remove-item'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
]