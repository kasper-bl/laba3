from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, verbose_name= 'информация о пользователе')

    def __str__(self):
        return f'Профиль {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()
    
    class Meta:
        ordering = ['-date_posted']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='comments')
    content = models.TextField(max_length=400, help_text="Напишите комментарий")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'Комментарий от {self.author} к "{self.post.title}"'
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Комментарий'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.post.pk})
