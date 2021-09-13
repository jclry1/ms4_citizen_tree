from django.contrib import admin

from .models import Donation, Price

admin.site.register(Donation) #Make project model available in Admin

admin.site.register(Price) #Make project model available in Admin
