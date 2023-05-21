from django.urls import path
from .views import otheruserProfile, follow_user
from contents.views import search

urlpatterns = [
    path('<int:pk>/', otheruserProfile , name='otheruser'),
    path('<int:user_to_follow>/follow/', follow_user , name='follow'),
    path('search/', search, name='search'),
] 