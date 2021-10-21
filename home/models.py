from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#https://learndjango.com/tutorials/django-best-practices-referencing-user-model
#https://stackoverflow.com/questions/57752859/django-user-object-has-no-attribute-profile
#https://stackoverflow.com/questions/1823880/relatedmanager-object-has-no-attribute

class Customer(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    stripe_customer_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)


# Create your models here.
