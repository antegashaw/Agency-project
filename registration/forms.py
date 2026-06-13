from django import forms
from .models import EmployeeApplication

class EmployeeApplicationForm(forms.ModelForm):
    class Meta:
        model = EmployeeApplication
        fields = [
            'full_name', 
            'gender', 
            'age', 
            'phone_number', 
            'region', 
            'education_level', 
            'destination_country', 
            'job_type'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ሙሉ ስምዎን እዚህ ያስገቡ'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ዕድሜ'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'የስልክ ቁጥር'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'education_level': forms.Select(attrs={'class': 'form-control'}),
            'destination_country': forms.Select(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
        }