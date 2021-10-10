from django.contrib import admin

from .models import Donation, Price, Donor

admin.site.register(Donation) #Make project model available in Admin

admin.site.register(Price) #Make project model available in Admin

admin.site.register(Donor) #Make project model available in Admin
