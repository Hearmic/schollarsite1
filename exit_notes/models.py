from datetime import timedelta
from django.utils import timezone
from django.db import models
from users.models import User
from django.urls import reverse


def get_deactivate_time():
    return timezone.now() + timedelta(minutes=15)


class exit_note(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    deactivate_on = models.DateTimeField(default=get_deactivate_time())
    created_by = models.ForeignKey(User, related_name='exit_note_created_by', on_delete=models.CASCADE, null=True, blank=True)
    parent_approved = models.ForeignKey(User, related_name='exit_note_parent_approved', on_delete=models.CASCADE, null=True, blank=True)
    teacher_approved = models.ForeignKey(User, related_name='exit_note_teacher_approved', on_delete=models.CASCADE, null=True, blank=True)
    security_approved = models.ForeignKey(User, related_name='exit_note_security_approved', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_denied = models.BooleanField(default=False)
    denied_by = models.ForeignKey(User, related_name='exit_note_denied_by', on_delete=models.CASCADE, null=True, blank=True)
    qr_code = models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('exit_notes_details', args=[str(self.id)])

    def __str__(self):
        return self.created_by.first_name + ' ' + self.created_by.last_name + ' ' + self.created_on.strftime('%Y-%m-%d %H:%M:%S') + ' ' + self.title
