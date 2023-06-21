from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['cover_photo', 'heading', 'subheadings', 'blog_text', 'conclusion']
