from django.db import models
from django.contrib.auth.models import User

class onlines(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='onlineUser')
    timestamp = models.DateTimeField()


