# forms.py
from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'fname', 'lname', 'gender', 'agree_terms', 'receive_newsletter']
        widgets = {
            'gender': forms.RadioSelect,
        }
