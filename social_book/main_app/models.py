from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import date
from .managers import CustomUserManager
from sqlalchemy import create_engine

# Create SQLAlchemy engine
engine = create_engine('postgresql://raj:root@localhost/social_book')
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    gender_choice = [
      ("Male", "Male"),
      ("Female", "Female"),
      ("Other","Other")
    ]
    
    credit_card_choices=[
        ("Visa", "Visa"),
        ("Mastercard", "Mastercard"),
        ("American Express", "American Express"),
        ("Discover", "Discover") 
    ]
    user_choices=[
      ("Auther","Auther"),
      ("Sellers","Sellers")
    ]
    
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(choices=gender_choice, max_length=255)
    user_type = models.CharField(choices = user_choices, max_length=50, blank=True,)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    credit_card_type = models.CharField(choices = credit_card_choices, max_length=255)
    credit_card_number = models.IntegerField()
    CVC = models.IntegerField()
    expiry_date = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    public_visibility = models.BooleanField(default=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if self.birth_year:
            today = date.today()
            self.age = today.year - self.birth_year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  address = models.CharField(max_length=255, default = 'NA')
  
class Books(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=500)
  visibility = models.BooleanField(default=True)
  cost = models.IntegerField()
  year_publish = models.IntegerField()
  file = models.FileField(upload_to='books/', null=True, default=None)
  