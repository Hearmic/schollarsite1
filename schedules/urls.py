from django.urls import path

from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.main, name='main'),
]