from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView

from .models import Post, Comment, Profile
from .forms import UserRegisterForm, PostForm

class HomePageView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_queryset(self):
        return Post.objects.all()
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'blog/register.html' 
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Пост успешно обновлен!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Пост успешно удален!')
        return super().delete(request, *args, **kwargs)