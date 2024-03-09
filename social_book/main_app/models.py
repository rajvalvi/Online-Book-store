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
    
    year_choice=[
      (2024,2024),
      (2025,2025),
      (2026,2026),
      (2027,2027),
      (2028,2028),
      (2029,2029),
      (2030,2030),
    ]
    
    
    
    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(choices=gender_choice, max_length=255, blank=True)
    user_type = models.CharField(choices = user_choices, max_length=50, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    credit_card_type = models.CharField(choices = credit_card_choices, max_length=255, blank=True)
    credit_card_number = models.BigIntegerField(blank=True, null=True)
    CVC = models.IntegerField(blank=True, null=True)
    expiry_month = models.IntegerField(choices = month_choice, blank=True, null=True)
    expiry_year = models.IntegerField(choices = year_choice, blank=True, null=True)
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
    
class Books(models.Model):
  user_id = models.IntegerField(null=True)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='cover_page/', null=True, default=None)
  description = models.CharField(max_length=500)
  visibility = models.BooleanField(default=True)
  cost = models.IntegerField()
  year_publish = models.IntegerField()
  file = models.FileField(upload_to='books/', null=True, default=None)
  