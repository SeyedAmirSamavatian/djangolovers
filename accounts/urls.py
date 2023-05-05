from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import registery , login_view , edit_profile, passwordChangeView


urlpatterns = [
    path('registery/', registery , name='registery'),
    path('login/', login_view , name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', edit_profile, name='edit_profile'),
    path('profile/change_pass', passwordChangeView.as_view(), name='change_pass'),
] 