from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment


class UserRegisterForm(UserCreationForm):  
    email = forms.EmailField(required=True)
    avatar = forms.ImageField 
    bio = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 3}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Расскажите о себе...'}),
        }

class PostForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):  
    class Meta:
        model = Comment
        fields = ['content']