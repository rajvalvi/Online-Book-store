from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def Register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            # return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register2.html', {'form': form})

# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import  authenticate, login
# # Create your views here.
# def Home(request):
#     return render (request, 'Home.html')

# def Login(request):
#     if request.method=='POST':
#         uname= request.POST.get('username')
#         pwd=request.POST.get('password')
#         user = authenticate(request, username=uname, password=pwd)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse("Invalid Credentials")

        
#     return render (request, 'login.html')

# def Register(request):
#     if request.method=='POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
#         if pass1!=pass2:
#             return HttpResponse("Password Missmatched")
#         else:
#             my_user = User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')
        
#     return render (request, 'register.html')