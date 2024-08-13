
from django.db import models
from django.contrib.auth.models import AbstractUser

        
class User(AbstractUser):
    surname = models.CharField(max_length=50, blank=True, null=True)
    parents = models.ManyToManyField('self', blank=True)
    head_teacher = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='teachers')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='myuser_set',  # Unique related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='myuser_set',  # Unique related name
        blank=True,
        help_text='Specific permissions for this user.',
    )
        
    def __str__(self):
        return f"{self.last_name} {self.first_name}  {self.surname}"

