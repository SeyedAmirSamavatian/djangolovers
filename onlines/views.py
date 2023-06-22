from django.shortcuts import render
from .models import onlines
from django.utils import timezone
from django.http import JsonResponse

def showOnline(request):
    user = request.user
    user_exists = onlines.objects.filter(user=user).exists()
    if user_exists:
        onlineUser = onlines.objects.get(user = user)
        onlineUser.timestamp = timezone.now()
        onlineUser.save();
        print('old User => ', onlineUser.timestamp)
    else:
        addUser = onlines(user=user, timestamp=timezone.now())
        addUser.save()
        print('new user => ', timezone.now())

    ten_seconds_ago = timezone.now() - timezone.timedelta(seconds=10)
    onlines_queryset = onlines.objects.filter(timestamp__gt=ten_seconds_ago) # gt=> greater than && lt => less than 
    dataOnline = []
    for userOnline in onlines_queryset:
        item = {
            'id': userOnline.user.id,
            'image': userOnline.user.profile.image.url,
            'first_name': userOnline.user.first_name,
            'last_name': userOnline.user.last_name,
        }
        dataOnline.append(item)
    return JsonResponse({'success': True,'dataOnline':dataOnline,})
