from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Books
from .forms import UploadBookForm
from django.shortcuts import render
from .models import engine
from sqlalchemy.sql import text
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
import json
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from main_app.decorators import check_uploaded_books
from .emails import *
import random
from django.conf import settings
from django.core.mail import send_mail

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            send_otp(request, user.email)
            request.session['email'] = email
            login(request, user)
            return redirect('verify_otp') 
        
        else:
            messages.success(request, 'Invalid email or password')
            form = CustomUserCreationForm()
    return render(request, 'login.html')

@login_required
def verify_otp(request):
    if request.method == 'POST':
        
        user_entered_otp = request.POST.get('otp')
        user_entered_otp=int(user_entered_otp)
        
        seesion_otp=request.session.get('otp')
        seesion_otp=int(seesion_otp)
        
        email1 = 'rajendravalvi2000@gmail.com'
        
        
        if (seesion_otp == user_entered_otp):
            login_detected(request,email1)
            return redirect('index') 
        else:
            messages.success(request, 'wrong OPT')
    return render(request, 'verify_otp.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required()
def index(request):
    username= request.user.user_name
    view_books = Books.objects.filter(visibility=True)
    return render (request, 'index.html',{'username':username, 'view_books': view_books})

@login_required()
def authors(request):
    author = CustomUser.objects.filter(public_visibility=True,user_type='Auther')
    return render(request, 'authors.html', {'author':author })

@login_required()
def sellers(request):
    Sellers = CustomUser.objects.filter(public_visibility=True,user_type='Sellers')
    return render(request, 'sellers.html', {'Sellers':Sellers })


@login_required()
def upload_book(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            if request.user.is_authenticated:
                book.user_id = request.user.id
            book.save()
            messages.success(request, 'Book uploaded successfully!')
            return redirect('upload_book')  # Redirect to a success URL
    else:
        form = UploadBookForm()
    return render(request, 'upload_book.html', {'form': form})

    


@login_required()
def view_all_book(request):
    view_books = Books.objects.filter(visibility=True)
    return render(request, 'view_all_book.html', {'view_books': view_books})


@login_required()
@check_uploaded_books
def view_user_books(request):
    view_books = Books.objects.filter(visibility=True,user_id=request.user.id)    
    return render(request, 'view_user_books.html', { 'view_books': view_books})

@login_required()
def fetch_data(request):
    with engine.connect() as connection:
        sql_query = text("SELECT * FROM main_app_books")
        result = connection.execute(sql_query)
        view_books = result.fetchall()
    return render(request, 'engine_data.html', {'view_books': view_books})

def logout_view(request):
    logout(request)
    return redirect('index')