from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)


class ChatBox(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chat')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chat')
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)