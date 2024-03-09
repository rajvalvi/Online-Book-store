from django import forms
from .models import CustomUser,Books
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(forms.ModelForm):
    # gender choice
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
    
    # Credit card choice
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
    
    #user type
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
    
    # expirory month
    month_choice=[
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
    ]
    
    expiry_month = forms.ChoiceField(
        choices = month_choice,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )
    
    # expiry year 
    year_choice=[
      (2024,2024),
      (2025,2025),
      (2026,2026),
      (2027,2027),
      (2028,2028),
      (2029,2029),
      (2030,2030),
    ]
    
    expiry_year = forms.ChoiceField(
        choices = year_choice,
        widget=forms.Select(attrs={
            'class':'form-control'
        })
    )
    
    
    class Meta:
        model = CustomUser
        fields = ['email', 'user_name', 'full_name', 'gender','user_type','public_visibility','birth_year', 'city', 'state', 'credit_card_type', 'credit_card_number', 'CVC', 'expiry_month', 'expiry_year', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'public_visibility':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            
        }
        
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if len(user_name) < 3:
            raise forms.ValidationError('Username must be at least 3 characters long.')
        return user_name

    def check_pasword(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('password must be at least 8 characters long.')
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    


class UploadBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'visibility', 'cost', 'year_publish','image', 'file']