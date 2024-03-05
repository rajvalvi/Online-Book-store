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

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            return HttpResponse("Invalid email or password.")
    return render(request, 'login.html')


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

def index(request):
    return render (request, 'index.html')


def sellers(request):
    Sellers = CustomUser.objects.filter(public_visibility=True,user_type='Sellers')
    return render(request, 'sellers.html', {'Sellers':Sellers })


def upload_book(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book uploaded successfully!')
            return redirect('upload_book')
    else:
        form = UploadBookForm()
    return render(request, 'upload_book.html', {'form': form})

def view_book(request):
    view_books = Books.objects.filter(visibility=True)
    return render(request, 'view_book.html', {'view_books': view_books})

def fetch_data(request):
    with engine.connect() as connection:
        sql_query = text("SELECT * FROM main_app_books")
        result = connection.execute(sql_query)
        view_books = result.fetchall()
    return render(request, 'engine_data.html', {'view_books': view_books})