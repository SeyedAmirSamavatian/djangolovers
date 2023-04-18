from django.urls import path
from .views import registery


urlpatterns = [
    path('registery/', registery , name='registery'),
] 