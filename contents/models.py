from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts')
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
    	return self.title