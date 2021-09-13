from django.db import models

# Based on: https://justdjango.com/blog/django-stripe-payments-tutorial

class Donation(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Price(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default = "desc")
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  #Note: Cents value

    def __str__(self):
        return self.description
	
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100) #Convert from cents to euros for display
