from django.urls import path
from .views import registery , login_view


urlpatterns = [
    path('registery/', registery , name='registery'),
    path('login/', login_view , name='login'),
] 