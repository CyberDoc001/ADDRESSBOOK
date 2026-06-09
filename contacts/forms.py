from django import forms
from .models import Contact, Group

class ContactForm(forms.ModelForm):
    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'secondary_phone',
            'address', 'city', 'state', 'country', 'zip_code',
            'company', 'job_title', 'website', 'birthday', 'notes',
            'photo', 'relationship', 'group', 'is_favorite'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 (555) 000-0000'}),
            'secondary_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Secondary phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State / Province'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP / Postal code'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job title'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add notes...'}),
            'relationship': forms.Select(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'is_favorite': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
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
