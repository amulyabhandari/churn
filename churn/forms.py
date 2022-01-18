from django import forms

class LoginForm(forms.Form) :
    username = forms.CharField(label='username', max_length=20)
    branch = forms.CharField(label='branch', max_length=30)
    password = forms.CharField(label='password', max_length=35, widget=forms.PasswordInput)
class SignupForm(forms.Form) :
    username = forms.CharField(label='username', max_length=20)
    branch = forms.CharField(label='branch', max_length=30)
    password = forms.CharField(label='password', max_length=35, widget=forms.PasswordInput)
    email = forms.CharField(label='email', max_length=50)
