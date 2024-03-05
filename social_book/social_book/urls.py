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
from main_app import views
# from apis import views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers
# from apis.views import *

# define the router
# router = routers.DefaultRouter()
 
# define the router path and viewset to be used
# router.register(r'geeks', GeeksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register, name='register'),
    path('index/',views.index, name='index'),
    path('login/',views.login_view, name='login'),
    path('authors/',views.authors, name='authors'),
    path('sellers/',views.sellers, name='sellers'),
    path('upload_book/',views.upload_book, name='upload_book'),
    path('view_book/',views.view_book, name='view_book'),
    path('fetch_data/',views.fetch_data, name='fetch_data'),
    # path('auth/', include('djoser.urls')),
    # path('', include("apis.urls")),
    # path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)