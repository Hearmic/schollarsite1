from django.urls import path

from exit_notes import views

app_name = 'exit_notes'

urlpatterns = [
    path('', views.view_notes, name='view_notes'),
    path('create/', views.create_note, name='create_note'),
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('<int:note_id>/', views.exit_notes_details, name='exit_notes_details'),
    path('<int:note_id>/parent_approve/', views.parent_approve, name="parent_approve"),
    path('<int:note_id>/teacher_approve/', views.teacher_approve, name="teacher_approve"),
    path('<int:note_id>/security_approve/', views.security_approve, name="security_approve"),
    path("<int:note_id>/deny/", views.deny, name="deny"),
    path('qr_code/<int:note_id>/', views.generate_qr_code, name='generate_qr_code'),
]
