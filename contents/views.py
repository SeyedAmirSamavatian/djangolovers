from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from .models import Post, PostComments
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpRequest
from .forms import PostForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def home(request):
    user_id = request.user.id
    posts = Post.objects.filter(author_id=user_id)
    # form = PostCommentForm(request.POST) #######################################
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


# @csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        author = request.user
        post = Post.objects.get(id=post_id)
        comment = PostComments(content=content, author=author, post=post)
        comment.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})



        
# @csrf_exempt
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(PostComments, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "post_edit.html"
    success_url = reverse_lazy('home')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)



def all_post(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'all_post.html', {'posts': posts})

from django.db.models import Q
def search(request):
    data = []
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search = request.POST.get('search')
        q = User.objects.filter(Q(first_name__icontains = search) | Q(last_name__icontains = search))
        if len(q) > 0 and len(search) > 0:
            for pos in q:
                item = {
                    'pk': pos.pk,
                    'first_name': pos.first_name,
                    'last_name': pos.last_name,
                    'img' : pos.profile.image.url, 
                }
                data.append(item)
        return JsonResponse({'success': True, 'data' : data})
    else:
        return JsonResponse({'success': False})