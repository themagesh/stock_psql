from django import forms
from .models import InputData
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InputDataForm(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['stockCode', 'companyName', 'industry', 'sector', 'website', 'about', 'singleLine', 'upTrend', 'downTrend','lineTouch', 'lineCross', 'live_price']

        # accounts/forms.py


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email']

    def username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('The username is already taken.')
        return username
    def stock_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('An account with this email already exists.')
        return email
    
    def clean_password2(self):
         password1 = self.cleaned_data.ge('password1') 
         password2= self.cleaned_data.get('password2') 
         username = self.cleaned_data.get('username')
         
         if password1 and password2 and password1 !=    password2:
             raise ValidationError('Password do not match.')
         if username.lower() in password1.lower():
             raise ValidationError('Password cannot contain username')
         return password2

def save(self, commit=True):
    user =  super().save(commit=False)
    user.set_password(self.cleaned_data['passsword1'])

    if commit:
        user.save()
    return user