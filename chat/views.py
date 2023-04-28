from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
from django.http import JsonResponse


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




