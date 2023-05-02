from django.urls import path
from .views import new_message, chat , chat_send, chat_update



urlpatterns = [
    path('<int:pk>/', new_message  , name='new_message'),
    path('<int:sender_id>/<int:recipient_id>/', chat  , name='chat'),
    path('send/', chat_send  , name='chat_send'),
    path('update/<int:recipient_id>/', chat_update  , name='chat_update'),
]
 