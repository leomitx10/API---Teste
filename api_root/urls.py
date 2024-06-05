"""
URL configuration for api_root project.

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

from api_rest.views import minha_view, minha_view_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'),name='api_rest_urls'),
    path('get/', minha_view, name='meu_link'),
    path('post/', minha_view_post, name='meu_linkd'),
    
]
