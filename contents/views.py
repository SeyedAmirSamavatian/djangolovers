from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpRequest
from .forms import PostForm



@login_required
def home(request):
    user_id = request.user.id
    posts = Post.objects.filter(author_id=user_id)
    return render(request, 'home.html', {'posts': posts})


@login_required
def deletePost(request, id):
    post_del  = Post.objects.get(id=id)
    if post_del.author_id == request.user.id:
        post_del.delete()
    posts = Post.objects.filter(author_id=request.user.id)
    return render(request, 'home.html', {'posts': posts})




@login_required
def likeDislike(request, post_id):
    if request.method == 'POST':
            post = Post.objects.get(id=post_id)
            user = request.user
            if user in post.likes.all():
                post.likes.remove(user)
                liked = False
            else:
                post.likes.add(user)
                liked = True
            likes_count = post.likes.count()
            posts = Post.objects.filter(author_id=request.user.id)
            liked_pro = []
            for index, like in enumerate(post.likes.all()):
                profile_Pic = f"<img src='{like.profile.image.url}' alt='{like.profile.image}' class='rounded-circle' style='width:30px;height: 30px;margin:0 -5px'>"
                liked_pro.append(profile_Pic)
                if index == 8:
                    break
            return JsonResponse({'success': True, 'liked': liked, 'likes_count': likes_count, 'liked_pro':liked_pro})
    return JsonResponse({'success': False})



@login_required
def send_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'send_post.html', {'form': form})


def SendComment(request):
    pass