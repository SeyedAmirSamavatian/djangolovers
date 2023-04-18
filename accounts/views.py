from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisteryUserForm
from django.contrib.auth.models import User

def registery(request):
	if request.method == 'POST':
		form = RegisteryUserForm(request.POST, request.FILES)
		if form.is_valid():
			email = form.cleaned_data['email']
			user_email_count = User.objects.filter(email = email).count()
			if user_email_count == 0 :
				form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username = username , password = password)
				login(request, user)
				return redirect('welcome')
			else:
				messages.success(request, (' کاربر با این ایمیل قبلا ثبت نام کرده است '))
	else:
		form = RegisteryUserForm()

	return render(request, 'registery.html' , {'form' : form})


