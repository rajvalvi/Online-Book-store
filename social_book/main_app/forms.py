from django import forms
from .models import CustomUser

from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(forms.ModelForm):
    gender_choice = [
      ("Male", "Male"),
      ("Female", "Female"),
      ("Other","Other"),
    ]
    
    gender = forms.ChoiceField(
        choices = gender_choice,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )
    
    credit_card_choices=[
        ("Visa", "Visa"),
        ("Mastercard", "Mastercard"),
        ("American Express", "American Express"),
        ("Discover", "Discover") 
    ]
    
    credit_card_type = forms.ChoiceField(
        choices = credit_card_choices,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )
    
    expiry_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'type':'date'
            }
        )
    )
    
    user_choices=[
      ("Auther","Auther"),
      ("Sellers","Sellers")
    ]
    
    user_type = forms.ChoiceField(
        choices = user_choices,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'user_name', 'full_name', 'gender','user_type','public_visibility','birth_year', 'city', 'state', 'credit_card_type', 'credit_card_number', 'CVC', 'expiry_date', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'public_visibility':forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
