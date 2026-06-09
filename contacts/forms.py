from django import forms
from .models import Contact, Group

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'state', 'country'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 (555) 000-0000'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State / Province'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Group name'}),
            'color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
        }

class SearchForm(forms.Form):
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'search-input',
        'placeholder': 'Search contacts...',
        'autocomplete': 'off',
    }))
