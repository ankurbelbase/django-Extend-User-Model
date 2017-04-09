from django import forms
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
	first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=False)
	last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=False)
	address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

	class Meta:
		model = User
		fields = ['first_name','last_name','address',]