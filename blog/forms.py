from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields =['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelsForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':2, 'placeholder': 'напишите комментарий(лучше не надо)'})
        }