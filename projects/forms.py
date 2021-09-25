from django import forms
from .models import Update, Project


class AddUpdate(forms.ModelForm):

    class Meta:
        model = Update
        fields = ('title', 'text', 'short_text', 'picture')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'short_text': forms.TextInput(attrs={'class': 'form-control'}),
        } 


#Form for updating the project details
class EditProject(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description', 'author', 'location', 'nursery', 'plantation',
                'species', 'available_to_partner', 'area_ha', 'started', 'picture')