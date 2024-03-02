from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'full_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
