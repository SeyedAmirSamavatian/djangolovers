from django.urls import path , include

from .views import home, deletePost, likeDislike, send_post, SendComment

urlpatterns = [
    path('', home , name='home'),
    path('new_post', send_post , name='new_post'),
    path('delete/<int:id>/', deletePost , name='delete_Post'),
    path('like-post/<int:post_id>/', likeDislike , name='like-post'),
    path('comment/<int:post_id>/', SendComment , name='send_comment'),
] 
