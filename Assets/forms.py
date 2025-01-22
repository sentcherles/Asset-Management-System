from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@testing.com'):
            raise forms.ValidationError("Only "testing" email addresses are allowed.")
        return email
