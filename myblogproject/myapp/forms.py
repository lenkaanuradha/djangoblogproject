from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User
from .models import Post

class Sign_upform(UserCreationForm):
 password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
 password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password(again)')
 class Meta:
    model=User
    fields=['username','last_name','first_name','email']
    labels={'email':'Email-address','username':'Name'}
    widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'})}
    
class loginform(AuthenticationForm):
  username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','autofocus':True}))
  password=forms.CharField(label="Password",strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))

class addform(forms.ModelForm):
  class Meta:
     model=Post
     fields=['title','desc']
     labels={'title':'Title','desc':'Description'}
     widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
              'desc':forms.Textarea(attrs={'class':'form-control'})}
class Postform(forms.ModelForm):
  class Meta:
     model=Post
     fields=['title','desc']
     labels={'title':'Title','desc':'Description'}
     widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
              'desc':forms.Textarea(attrs={'class':'form-control'})}
 