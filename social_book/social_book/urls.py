"""
URL configuration for social_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main_app import views as main_app
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest
from django.views.decorators.csrf import csrf_exempt
# from django.views import CustomTokenLoginView
from django.urls import path, include
from apis import views as ap
from main_app.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',main_app.register, name='register'),
    path('index/',main_app.index, name='index'),
    path('login/',main_app.login_view, name='login'),
    path('authors/',main_app.authors, name='authors'),
    path('sellers/',main_app.sellers, name='sellers'),
    path('upload_book/',main_app.upload_book, name='upload_book'),
    path('view_all_book/',main_app.view_all_book, name='view_all_book'),
    path('view_user_books/',main_app.view_user_books, name='view_user_books'),
    path('fetch_data/',main_app.fetch_data, name='fetch_data'),
    path('logout/', main_app.logout_view, name='logout'),
    
    path('verify_otp/',main_app.verify_otp, name='verify_otp'),
    #api
    path('api/', include('apis.urls')),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)