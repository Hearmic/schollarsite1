import qrcode
from datetime import timedelta
from django.db.models import Q
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import ExitNote, ExitPass, Exits 
from .forms import ExitNoteForm, DayTimeSlotFormSet
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from schollarsite.decorators import allowed_user_groups



@login_required
def exit_notes_main(request): 
    context = {
        'passes': get_valid_passes_for_user(request),
        'notes': get_valid_notes_for_user(request),
        'debug_state': settings.DEBUG
    }
    return render(request, 'exit_notes/exit_notes_main.html', context)

def request_exit_note(request):
    user = request.user
    if request.method == 'POST':
        form = ExitNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = user
            note.teacher = user.grade.head_teacher if user.grade else None
            note.save()
    return render(request, 'exit_notes/request_note.html')
def get_valid_notes_for_user(request):
    user = request.user
    notes = ExitNote.objects.filter(
        Q(student=user) |
        Q(parent=user) |
        Q(teacher=user)
    )
    valid_notes = notes.filter(deactivate_on__gt=timezone.now() - timedelta(hours=6))
    return valid_notes


@login_required
@allowed_user_groups(['Родитель','Системный администратор'])
def parent_approve_note(request, note_id):
    if request.method == 'POST':
        user = request.user
        note = ExitNote.objects.get(pk=note_id)
        note.parent_approved = user
        note.save()
    return 


@login_required
@allowed_user_groups(['Учитель','Классный руководитель','Системный администратор'])
def teacher_approve_note(request, note_id):
    if request.method == 'POST':
        note = ExitNote.objects.get(pk=note_id)
        user = request.user
        note.teacher_approved = user
        note.save()
    return 

@login_required
@allowed_user_groups(['Безопасность','Системный администратор'])
def confirm_exit_note(request, note_id):
    if request.method == 'POST':
        exit = Exits(
            type=ExitNote,
            exit_note=ExitNote.objects.get(pk=note_id),
            sequrity_approved=request.user,
        )
        exit.save()
    return 


@login_required
def generate_qr_code_note(request, pass_id):
    details_url = request.build_absolute_uri(reverse('exit_notes:exit_notes_details', args=[pass_id]))
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(details_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response


@login_required
@allowed_user_groups(['Родитель','Учитель','Безопасность'])
def deny_note(request, note_id):
    note = ExitNote.objects.get(pk=note_id)
    user = request.user
    note.is_denied = True
    note.denied_by = user
    note.save()
    return 


def get_valid_passes_for_user(request):
    user = request.user
    current_day = timezone.localtime().strftime('%A')  
    current_time = timezone.localtime().time() 
    passes = ExitNote.objects.filter(
        Q(student=user) | Q(parent=user) | Q(teacher=user),
        is_active=True,
        day_time_slots__day_of_week=current_day,
        day_time_slots__start_time__lte=current_time,
        day_time_slots__end_time__gte=current_time
    ).distinct()
    valid_passes = passes.filter(passes.day_time_slots.day_of_week == current_day)
    return valid_passes


@login_required
@allowed_user_groups(['Системный адмниистратор', 'Школьная адмнистрация', 'Систеный адмнистратор', 'Классный руководитель'])
def create_or_update_exit_pass(request, pass_id=None):
    if pass_id:
        exit_pass = ExitPass.objects.get(id=pass_id)
    else:
        exit_pass = ExitPass()
    if request.method == 'POST':
        formset = DayTimeSlotFormSet(request.POST, instance=exit_pass)
        if formset.is_valid():
            exit_pass.save()  # Сохраняем родительский объект
            formset.save()  # Сохраняем дочерние объекты
            return redirect('success_url')  # Перенаправление после сохранения
    else:
        formset = DayTimeSlotFormSet(instance=exit_pass)

    return render(request, 'exit_pass_form.html', {'formset': formset})


@login_required
@allowed_user_groups(['Родитель','Системный администратор'])
def parent_approve(request, pass_id):
    if request.method == 'POST':
        user = request.user
        exit_pass = ExitNote.objects.get(pk=pass_id, parent=user)
        exit_pass.parent_approved = True
        exit_pass.save()
    return 


@login_required
@allowed_user_groups(['Классный руководитель', 'Учитель', 'Системный администратор'])
def teacher_approve_pass(request, pass_id):
    if request.method == 'POST':
        user = request.user
        exit_pass = ExitPass.objects.get(pk=pass_id, teacher=user)
        exit_pass.teacher_approved = True
        exit_pass.save()
    return


@login_required
@allowed_user_groups(['Школьная администрация','Системиный администратор'])
def activate_pass(request, pass_id):
    if request.method == 'POST':
        exit_pass = ExitPass.objects.get(pk=pass_id)
        exit_pass.is_active = True
        exit_pass.save()
    return


@login_required
@allowed_user_groups(['Безопасность', 'Школьная администрация', 'Системный администратор'])
def exit_pass_delails(request, pass_id):
    exit_pass = ExitPass.objects.get(pk=pass_id)
    context = {'exit_pass': exit_pass}
    return render (request, 'exit_notes/exit_pass_details.html', context)


@login_required
def generate_qr_code_pass(request, pass_id):
    details_url = request.build_absolute_uri(reverse('exit_notes:exit_pass_details', args=[pass_id]))
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(details_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response


@login_required
def how_it_works(request):
    context = {
        'moderators': ['Модератор предложений', 'Школьная администрация', 'Системный администратор'],
        'students': ['Ученик'],
        'teachers': ['Учитель', 'Классный руководитель', 'Завуч'],
        'parents': ['Родитель']
        }
    return render(request, 'exit_notes/how_it_works.html', context)
