from django.contrib import admin
from .models import Project, Update

@admin.register(Project) #Make project model available in Admin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }

@admin.register(Update) #Make project model available in Admin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'update_slug': ('title',), }
