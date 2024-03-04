from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home') 
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

def home(request):
    return render (request, 'Home.html')


def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True)
    author = CustomUser.objects.filter(public_visibility=True,user_type='Auther')
    Sellers = CustomUser.objects.filter(public_visibility=True,user_type='Sellers')
    return render(request, 'authors_and_sellers.html', {'users': users,'author':author,'Sellers':Sellers })