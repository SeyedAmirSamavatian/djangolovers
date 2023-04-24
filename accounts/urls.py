from django.urls import path
from .views import registery , login_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('registery/', registery , name='registery'),
    path('login/', login_view , name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
] 