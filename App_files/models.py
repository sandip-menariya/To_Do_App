from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Task(models.Model):
    CHOICES=[
        ('pending','Pending'),
        ('completed','Completed'),
        ('in_progress','In Progress'),
    ]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=CHOICES,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
