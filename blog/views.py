from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, Profile

class HomePageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_queryset(self):
        return Post.objects.all()
    
class PostDetailView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'