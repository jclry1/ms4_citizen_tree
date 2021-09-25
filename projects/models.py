from django.conf import settings #Necessary due to custom user model: https://learndjango.com/tutorials/django-best-practices-referencing-user-model
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, DecimalField, EmailField
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Class-based view for projects based on: https://www.youtube.com/watch?v=RwWhQTSV44Q

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'projects')
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=80)
    nursery = BooleanField(default=False)
    plantation = BooleanField(default=False)
    species = CharField(max_length=180, null=True)
    available_to_partner = BooleanField(default=True)
    area_ha = DecimalField(max_digits=3, decimal_places=2)
    project_lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contact = EmailField()
    started = DateField()
    picture = models.FileField(upload_to='media/', default='media/default.jpg', blank=True)

    def get_absolute_url(self):
        return reverse('projects:spotlight', kwargs={'slug': self.slug})


    class Meta:
        ordering=['-published']


    def __str__(self):
        return self.title

class Update(models.Model):
    title = models.CharField(max_length=100, null=False)
    update_slug = models.SlugField(max_length=100, unique=False)
    text = models.TextField(null=False)
    short_text = models.TextField(max_length=150)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, default='1', on_delete=models.CASCADE)
    picture = models.FileField(upload_to='media/', default='media/default-2.jpg', blank=True)



    def get_absolute_url(self):
        return reverse('projects:report', kwargs={"id":self.id})


    """ def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs) """ 

    class Meta:
        ordering = ['-date_added']   


    def __str__(self):
        return self.title