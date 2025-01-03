"""
URL configuration for schollarsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import redirect_to_login


urlpatterns = [
    path('', redirect_to_login),
    path("select2/", include("django_select2.urls")),
    path('home/', include('main.urls', namespace='main')),
    path('admin/', admin.site.urls),
    path('suggestions/', include('suggestions.urls', namespace='suggestions')),
    path('schedules/', include('schedules.urls', namespace='schedulers')),
    path('exit_notes/', include('exit_notes.urls', namespace='exit_notes')),
    path('users/', include('users.urls', namespace='users')),
    path('menu/', include('canteen_menu.urls', namespace='menu')),
    path('schedules/', include('schedules.urls', namespace='schedules')),
    path('news/', include('news.urls', namespace='news')),
]
