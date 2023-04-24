from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisteryUserForm, LoginForm
from django.contrib.auth.models import User

def registery(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = RegisteryUserForm(request.POST, request.FILES)
		if form.is_valid():
			email = form.cleaned_data['email']
			user_email_count = User.objects.filter(email = email).count()
			if user_email_count == 0 :
				form.save()
				username = form.cleaned_data['email']
				password = form.cleaned_data['password1']
				user = authenticate(username = username , password = password)
				login(request, user)
				return redirect('home')
			else:
				messages.success(request, (' کاربر با این ایمیل قبلا ثبت نام کرده است '))
	else:
		form = RegisteryUserForm()

	return render(request, 'registery.html' , {'form' : form})


def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = authenticate(request, username = email, password = password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.success(request, 'ایمیل یا پسورد اشتباه است')
	else:
		form = LoginForm()
	return render(request, "login.html", {'form':form})

