from django.urls import path

from calender import views

app_name = 'calender'

urlpatterns = [
    path('',views.calender, name='calender_main')
]
