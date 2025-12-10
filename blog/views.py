from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView

from .models import Post, Comment, Profile
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.decorators import login_required

class HomePageView(ListView):

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_queryset(self):
        return Post.objects.all()
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Обработка комментария
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Для комментариев нужно войти в систему')
            return redirect('login')
        
        content = request.POST.get('content', '').strip()
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )

        messages.success(request, 'Комментарий добавлен!')
        return redirect('post_detail', pk=pk)
    
    # GET запрос
    comments = post.comments.all().order_by('-created_at')
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
})

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
    
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.info(request, 'Лайк убран')
    else:
        post.likes.add(request.user)
        messages.success(request, 'Лайк добавлен')
    
    return redirect('post_detail', pk=pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    
    if comment.author != request.user:
        messages.error(request, 'Вы не можете удалить этот комментарий')
    else:
        comment.delete()
        messages.success(request, 'Комментарий удален')
    
    return redirect('post_detail', pk=post_pk)