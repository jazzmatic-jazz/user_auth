from django import forms
from .models import User, Address
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator


class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(), label="Password")
	confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

	line1 = forms.CharField(widget=forms.TextInput(), label="Address Line 1")
	city = forms.CharField(widget=forms.TextInput(), label="City")
	state = forms.CharField(widget=forms.TextInput(), label="State")
	pin_code = forms.IntegerField(
        validators=[
            MinValueValidator(100000, message="6 digits"),
            MaxValueValidator(999999, message="6 digits"),
        ],
        label="PIN Code"
    )

	class Meta:
		model = User
		fields = [ "first_name",  'last_name' , 'profile_picture', 'username', 'email', 'user_type', 'password', 'confirm_password']

	
	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')
		if password and confirm_password and  password != confirm_password:
			self.add_error('confirm_password', 'Password does not match.')
		
	def save(self, commit=True):
		user = super().save(commit=False)
		user.password = make_password(self.cleaned_data["password"])
		if commit:
			user.save()
			Address.objects.create(
                user=user,
                line1=self.cleaned_data["line1"],
                city=self.cleaned_data["city"],
                state=self.cleaned_data["state"],
                pin_code=self.cleaned_data["pin_code"],
            )

		return user

	
