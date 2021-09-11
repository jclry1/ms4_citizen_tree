from django import forms
from .models import Update


class AddUpdate(forms.ModelForm):

    class Meta:
        model = Update
        fields = ('title', 'text', 'short_text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'short_text': forms.TextInput(attrs={'class': 'form-control'}),
        } 