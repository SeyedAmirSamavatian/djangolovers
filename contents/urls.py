from django.urls import path , include

from .views import home, deletePost, likeDislike, send_post, add_comment, delete_comment, PostUpdateView, all_post, search

urlpatterns = [
    path('', home , name='home'),
    path('new_post', send_post , name='new_post'),
    path('delete/<int:id>/', deletePost , name='delete_Post'),
    path('like-post/<int:post_id>/', likeDislike , name='like-post'),
    path('add_comment/', add_comment, name='add_comment'),
    path('<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('all_post/', all_post, name='all_post'),
    path('search/', search, name='search'),
] 

