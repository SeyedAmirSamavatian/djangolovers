from django.shortcuts import render



def welcome(request):
	return render(request,'index.html')




def base(request):
	return render(request,'base.html')