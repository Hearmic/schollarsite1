import qrcode
from datetime import timedelta
from django.db.models import Q
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from .models import exit_note
from .forms import ExitNoteForm
from django.contrib.auth.decorators import login_required
from users.models import Grade
from django.conf import settings
from django.urls import reverse
@login_required
def exit_notes_main(request):
    user = request.user
    form = ExitNoteForm()
    try:
        user_grade = Grade.objects.get(students=user)
    except Grade.DoesNotExist:
        user_grade = None

    user_grade_students = user_grade.students.all() if user_grade else []
    notes = exit_note.objects.filter(
        Q(created_by=user) |
        Q(created_by__in=user.parents.all()) |
        Q(created_by__in=user_grade_students)
    )
    valid_notes = notes.filter(created_on__gt=timezone.now() - timedelta(hours=6))
    
    context = {
        'valid_notes': valid_notes,
        'form': form,
        'debug_state': settings.DEBUG 
    }

    if request.method == 'POST':
        form = ExitNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = user
            note.head_teacher = user_grade.head_teacher if user_grade else None
            note.save()
            return redirect('exit_notes:exit_notes')
    return render(request, 'exit_notes/exit_notes_main.html', context)

@login_required
def exit_notes_details(request, note_id):
    note = exit_note.objects.get(pk=note_id)
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render (request, 'exit_notes/exit_note_details.html' , context)

@login_required
def parent_approve(request,note_id):
    if request.method == 'POST':
        note = exit_note.objects.get(pk=note_id)
        user = request.user
        note.parent_approved = user
        note.save()
    return redirect('exit_notes:exit_notes')

@login_required
def teacher_approve(request,note_id):
    if request.method == 'POST':
        note = exit_note.objects.get(pk=note_id)
        user = request.user
        note.teacher_approved = user
        note.save()
    return redirect('exit_notes:exit_notes')

@login_required
def security_approve(request,note_id):
    if request.method == 'POST':
        note = exit_note.objects.get(pk=note_id)
        user = request.user
        note.security_approved = user
        note.is_active = False
        note.save()
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'security':['Безопасность','Охранник']
        }
    return render(request, 'exit_notes/exit_note_details.html', context)

@login_required 
def generate_qr_code(request, note_id):
    # Fetch the note
    note = get_object_or_404(exit_note, id=note_id)
    
    # Construct the details page URL
    details_url = request.build_absolute_uri(reverse('exit_notes:exit_notes_details', args=[note_id]))
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(details_url)
    qr.make(fit=True)

    # Create an image for the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Return the image as an HTTP response
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

@login_required
def deny(request, note_id):
    note = exit_note.objects.get(pk=note_id)
    user = request.user
    note.is_denied = True
    note.denied_by = user
    note.save()
    context = {
        'note': note,
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render(request, 'exit_notes/exit_note_details.html', context)

@login_required
def how_it_works(request):
    context = {
        'moderators': ['Модератор предложений','Школьная администрация','Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель','Классный руководитель', 'Завуч'],
        'parents':['Родитель']
        }
    return render (request, 'exit_notes/how_it_works.html' , context)