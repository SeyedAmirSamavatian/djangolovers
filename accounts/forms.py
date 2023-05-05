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




class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(required=True, max_length=30)
	last_name = forms.CharField(required=True, max_length=30)
	image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange': 'previewImage(event)'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'image')

	def save(self, commit=True):
		user = super(UpdateUserForm, self).save(commit=False)
		if commit:
			user.save()
			try:
				profile = user.profile
			except Profile.DoesNotExist:
				profile = Profile(user = user)
			if self.cleaned_data['image'] is not None:
				profile.image = self.cleaned_data['image']
			profile.save()
		return user



from django.contrib.auth.forms import PasswordChangeForm
class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(label='پسورد فعلی' , widget = forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label='پسورد جدید' , widget = forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label='تکرار پسورد جدید' , widget = forms.PasswordInput(attrs={'class':'form-control'}))