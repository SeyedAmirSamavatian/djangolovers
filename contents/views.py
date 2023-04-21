from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})