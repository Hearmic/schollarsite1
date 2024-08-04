from django.db import models
from users.models import User

class Requests(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    office_number = models.IntegerField(verbose_name= "Номер кабинета", null=True, blank=True)
    office_name = models.CharField(max_length=255, verbose_name= "Название кабинета", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_moderated = models.BooleanField(default=False) 
    is_denied = models.BooleanField(default=False)
    denial_reason = models.CharField(max_length=100, verbose_name= "Причина отказа", null=True, blank=True) 
    is_complete = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)
    completed_by = models.ForeignKey (User, on_delete=models.CASCADE, null=True, blank=True, related_name='completed_by')
    
                                
    def __str__(self):
        return self.title
    