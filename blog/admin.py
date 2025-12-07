from django.contrib import admin
from .models import Post, Comment, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'title', 'total_likes_display')
    list_filter = ('created_at', 'author')
    date_hierarchy = 'created_at'

    def total_likes_display(self, obj):
        return obj.total_likes()
    
    total_likes_display.short_description = 'Лайки'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'created_at')
    list_filter = ('created_at',)

admin.site.register(Profile)