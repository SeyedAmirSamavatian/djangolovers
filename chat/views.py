from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Message, ChatBox 
from django.db.models import Q

@login_required
def new_message(request,pk):
	if request.method == 'POST':
		sender_message = int(request.POST.get('sender_id'))
		recipient_message = int(request.POST.get('recipient_id'))

		if request.user.id == sender_message:

			message = request.POST.get('message')
			sender_id = User.objects.get(id=sender_message)
			recipient_id = User.objects.get(id=recipient_message)

			sendMessage = Message(sender=sender_id, recipient = recipient_id, message= message)
			sendMessage.save()

			return JsonResponse({'success': True,'alert':' پیام شما با موفقیت ارسال شد'})
	else:
		return JsonResponse({'success': False})	




@login_required
def chat(request, sender_id, recipient_id):
	chats = ChatBox.objects.filter((Q(sender_id=sender_id) & Q(recipient_id=recipient_id)) | (Q(sender_id=recipient_id) & Q(recipient_id=sender_id))).order_by('timestamp', 'id')
	allChats = ChatBox.objects.filter((Q(sender_id=request.user.id))|(Q(recipient_id=request.user.id)))
	list_id = []
	for chat in allChats:
		list_id.append(chat.sender.id)
		list_id.append(chat.recipient.id)
	list_id = list(set(list_id))

	All_User_Chat = User.objects.filter(Q(id__in=list_id) & ~Q(id = request.user.id))
	return render(request, 'chat.html', {'chats':chats, 'All_User_Chat':All_User_Chat, 'sender_id':sender_id , 'recipient_id':recipient_id})


@login_required
def chat_send(request):
	if request.method == 'POST':
		sender_message = int(request.POST.get('sender_id'))
		recipient_message = int(request.POST.get('recipient_id'))
		if request.user.id == sender_message:

			message = request.POST.get('chatText')
			sender_id = User.objects.get(id=sender_message)
			recipient_id = User.objects.get(id=recipient_message)

			sendMessage = ChatBox(sender=sender_id, recipient = recipient_id, message= message)
			sendMessage.save()

			return JsonResponse({'success': True,'alert':' پیام شما با موفقیت ارسال شد'})
	else:
		return JsonResponse({'success': False})	


import json
from django.views.decorators.csrf import csrf_exempt
@login_required
# @csrf_exempt
def chat_update(request, recipient_id):
	user_recipient = User.objects.get(id=recipient_id)
	img_recipient = user_recipient.profile.image.url
	first_name_recipient = user_recipient.first_name
	user_sender = User.objects.get(id=request.user.id)
	img_sender = user_sender.profile.image.url
	first_name_sender = user_sender.first_name


	if request.method == 'POST':
		sender_message = request.user.id
		recipient_message = recipient_id

		chats = ChatBox.objects.filter((Q(sender_id=sender_message) & Q(recipient_id=recipient_message)) | (Q(sender_id=recipient_message) & Q(recipient_id=sender_message))).order_by('timestamp', 'id')
		chats_list = list(chats.values())
		dataChat = []
		for chat in chats_list:
			dataChat.append(chat)
		return JsonResponse({'success': True,'first_name_sender':first_name_sender,'first_name_recipient':first_name_recipient, 'img_recipient' : img_recipient, 'img_sender':img_sender, 'dataChat':dataChat})
	else:
		return JsonResponse({'success': False})	