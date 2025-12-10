from django.contrib import admin
from .models import Profile, Post, Comment

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']
    search_fields = ['user__username', 'bio']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted', 'total_likes', 'total_comments']
    list_filter = ['date_posted', 'author']
    search_fields = ['title', 'content']
    date_hierarchy = 'date_posted'
    filter_horizontal = ['likes']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at', 'updated_at']
    list_filter = ['created_at', 'author']
    search_fields = ['content', 'post__title']
    date_hierarchy = 'created_at'