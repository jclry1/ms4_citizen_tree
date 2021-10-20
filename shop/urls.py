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
    path('payment/stripe/', views.StripePaymentView.as_view(), name='stripe-pay'),
    path('webhooks/stripe/', views.stripe_webhook_view, name='stripe-webhook'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path ('orders/<pk>/', views.OrderReview.as_view(), name='order-review'),
]