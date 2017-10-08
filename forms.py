from trend_promotion.models import *
from django import forms
from django.forms import ModelForm, Textarea

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'phone_number', 'twitter_name', 'current_city']

