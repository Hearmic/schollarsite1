from datetime import timedelta
from django.forms import ValidationError
from django.utils import timezone
from django.db import models
from users.models import User
from django.urls import reverse


def get_deactivate_time():
    return timezone.now() + timedelta(minutes=40)


def user_deleted_message():
    return "Пользователь был удален"


def note_deleted_message():
    return "Запись была удалена"


class ExitNote(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deactivate_on = models.DateTimeField(default=get_deactivate_time())
    student = models.ForeignKey(User, related_name='exit_note_student', on_delete=models.SET(user_deleted_message), null=True, blank=True)
    parent = models.ForeignKey(User, related_name='exit_note_parent', on_delete=models.SET(user_deleted_message), null=True, blank=True)
    teacher = models.ForeignKey(User, related_name='exit_note_teacher', on_delete=models.SET(user_deleted_message), null=True, blank=True)
    parent_approved = models.BooleanField(default=False)
    teacher_approved = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    denied_by = models.ForeignKey(User, related_name='exit_note_denied_by', on_delete=models.SET(user_deleted_message), null=True, blank=True)

    def get_absolute_url(self):
        return reverse('exit_notes_details', args=[str(self.id)])

    def __str__(self):
        return f'{self.title} {self.student.first_name} {self.student.last_name} {self.created_on.strftime('%Y-%m-%d %H:%M:%S')}'


class ExitPass(models.Model):
    title = models.CharField(max_length=255, default='Пропуск на выход для ученика школы "Престиж"')
    student = models.ForeignKey(User, related_name='exit_pass_student', on_delete=models.SET(user_deleted_message), blank=True, null=True)
    parent = models.ForeignKey(User, related_name='exit_pass_parent', on_delete=models.SET(user_deleted_message), blank=True, null=True) 
    teacher = models.ForeignKey(User, related_name='exit_pass_teacher', on_delete=models.SET(user_deleted_message), blank=True, null=True)
    parent_approved = models.BooleanField(default=False, null=True)
    teacher_approved = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.title} {self.student.first_name} {self.student.last_name} {self.date.strftime("%Y-%m-%d %H:%M:%S")}'


class DayTimeSlot(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
    ]

    exit_pass = models.ForeignKey(ExitPass, related_name='day_time_slots', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.day_of_week}: {self.start_time} - {self.end_time} for {self.exit_pass.title}'


class Exits(models.Model):
    EXIT_TYPES = [
        ('ExitNote', 'Записка'),
        ('ExitPass', 'Пропуск'),
    ]

    type = models.CharField(choices=EXIT_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    sequrity_approved = models.ForeignKey(User, related_name='approved_exit', on_delete=models.CASCADE)
    exit_note = models.ForeignKey(ExitNote, related_name='note', on_delete=models.SET(note_deleted_message), null=True, blank=True)
    exit_pass = models.ForeignKey(ExitPass, related_name='pass', on_delete=models.SET(note_deleted_message), null=True, blank=True)

    def clean(self):
        super().clean()
        if not self.exit_note and not self.exit_pass:
            raise ValidationError("Вы должны связать хотя бы один обьект.")
        if self.exit_note and self.exit_pass:
            raise ValidationError("Вы можете связать только один обьект.")
    
    def __str__(self):
        if self.exit_note:
            return self.type + self.date.strftime('%Y-%m-%d %H:%M:%S') + f'Для:{self.exit_note.student.last_name} {self.exit_note.student.first_name}' + ' ' + f'Подтверждена:{self.sequrity_approved.last_name} {self.sequrity_approved.first_name}' 
        if self.exit_pass:
            return self.type + self.date.strftime('%Y-%m-%d %H:%M:%S') + f'Для:{self.exit_pass.student.last_name} {self.exit_pass.student.first_name}' + ' ' + f'Подтверждена:{self.sequrity_approved.last_name} {self.sequrity_approved.first_name}'

