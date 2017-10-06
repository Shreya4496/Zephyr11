from trend_promotion.models import *
from django import forms
from django.forms import ModelForm, Textarea

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'phone_number', 'twitter_name', 'current_city']

class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = '__all__'
        widgets = {
            'complaint_description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        print (""+fields)
        # print("jaclin")

        def __init__(self):
            self.fields['first_name'].label = "First Name"