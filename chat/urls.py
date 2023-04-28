from django.urls import path
from .views import new_message 



urlpatterns = [
    path('<int:pk>/', new_message  , name='new_message'),
] 