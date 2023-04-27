from django.shortcuts import render
from accounts.models import Profile
from contents.models import Post
from datetime import datetime, timezone

from django.shortcuts import render, get_object_or_404
from .models import User, Follower

def timePass(time): 
	last_login_time = time
	last_login_time = last_login_time.astimezone(timezone.utc)
	current_time = datetime.now(timezone.utc)
	time_diff = current_time - last_login_time

	days = time_diff.days
	hours, remainder = divmod(time_diff.seconds, 3600)
	minutes, _ = divmod(remainder, 60)

	time_diff_str = f"last user login: {days} d, {hours} h, {minutes} m, ago"
	return time_diff_str

def otheruserProfile(request, pk):
	user_id = pk;
	profiles = Profile.objects.get(user_id=user_id)

	lastLogin = timePass(profiles.user.last_login)

	posts = Post.objects.filter(author_id=user_id)
	num = 0
	for post in posts:
		num += post.likes.count()

	users = User.objects.all()
	followers = Follower.objects.filter(following_id = user_id)
	following = []
	for follow in followers:
		print(follow.follower.id)
		following.append(follow.follower.id)
	return render(request, 'otheruser.html', {'profiles':profiles, 'posts':posts, 'lastLogin':lastLogin, 'Get_likes':num, 'users':users, 'following': following})


from django.http import JsonResponse
def follow_user(request, user_to_follow):
	user_to_follow = get_object_or_404(User, id=user_to_follow)
	if request.user != user_to_follow:
		follower, created = Follower.objects.get_or_create(follower=request.user, following=user_to_follow)
		follow = 'Unfollow'
		if not created:
			follower.delete()
			follow = 'Follow'
	return JsonResponse({'success': True, 'follow': follow })
