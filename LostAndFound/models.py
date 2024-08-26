from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    found_in = models.IntegerField()
    found_at = models.DateTimeField(auto_now_add=True)
