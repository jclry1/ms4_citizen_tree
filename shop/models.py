from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

User = get_user_model()

class VarietySpec(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    created = models. DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    bareroot = models.BooleanField(default = True)
    picture = models.FileField(upload_to='media/', default='media/default.jpg', blank=True)
    available_varieties = models.ManyToManyField(VarietySpec)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product-spotlight", kwargs={'slug': self.slug })

    def get_display_price(self):
        return "{:.2f}".format(self.price / 100) #Convert from cents to euros for display, same convention as for donations 

class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length = 120)
    address_line_2 = models.CharField(max_length = 120)
    address_line_3 = models.CharField(max_length = 120)
    county = models.CharField(max_length = 32)
    eircode = models.CharField(max_length=7)
    default = models.BooleanField(default=False)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)

    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.address_line_3}, {self.eircode}"

    class Meta:
        verbose_name_plural = 'Addresses'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey("Order", related_name='items', on_delete=models.CASCADE)
    variety = models.ForeignKey(VarietySpec, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.product.title} by {self.quantity}"

    def get_raw_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_item_price_display(self):
        price = self.get_raw_total_item_price()
        return "{:.2f}".format(price / 100)


    

class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(
        Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)    

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"ORDER-{self.pk}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=(
        ('Stripe','Stripe'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.reference_number

    @property
    def reference_number(self):
        return f"PAYMENT-{self.order} - {self.pk}"


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug - slugify(instance.title)


pre_save.connect(pre_save_product_receiver, sender = Product)