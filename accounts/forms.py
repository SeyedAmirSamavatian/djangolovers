from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisteryUserForm(UserCreationForm):
	email = forms.EmailField(label='ایمیل')
	image = forms.ImageField(required =False)
	class Meta:
		model = User
		fields = ('first_name', 'last_name','email', 'password1', 'password2', 'image')

	def save(self, commit=True):
		user = super(RegisteryUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['email']
		if commit:
			user.save()
			profile = Profile(user=user, image=self.cleaned_data.get('image'))
			profile.save();
		return user

class LoginForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(widget = forms.PasswordInput)