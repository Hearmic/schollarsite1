from django.urls import path
from . import views  

app_name = 'repair_requests'

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('', views.request_list, name='request_list'),
    path('unmoderated/', views.unmoderated_request_list, name='unmoderated_request_list'),
    path('moderate/<int:requests_id>', views.moderate_request, name='moderate_request'),
    path('delete/<int:requests_id>', views.delete_request, name='delete_request'),
    path('requset/<int:requests_id>', views.request_detail, name='request_detail'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('deny/<int:requests_id>', views.deny_request, name='deny_request'),
    path('mark_complete/<int:requests_id>', views.mark_complete, name='mark_complete'),
]
