from django.urls import path
from .views import new_message, chat , chat_send, chat_update, delete_chat, privateMessage, userPrivate_message, Del_Private_message



urlpatterns = [
    path('<int:pk>/', new_message  , name='new_message'),
    path('<int:sender_id>/<int:recipient_id>/', chat , name='chat'),
    path('send/', chat_send  , name='chat_send'),
    path('update/<int:recipient_id>/', chat_update  , name='chat_update'),
    path('delete/<int:id>/', delete_chat  , name='delete_chat'),
    path('privateMessage/', privateMessage  , name='privateMessage'),
    path('privateMessage/<int:id>/', userPrivate_message  , name='userPrivate_message'),
    path('privateMessage/delete/<int:id>/<int:sender_id>', Del_Private_message  , name='Del_Private_message'),
]
