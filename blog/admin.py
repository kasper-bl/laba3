from django.contrib import admin
from .models import Post, Comment, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['']