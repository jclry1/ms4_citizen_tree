from django.contrib import admin
from .models import Project

@admin.register(Project) #Make project model available in Admin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }


# Register your models here.
