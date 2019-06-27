from django.contrib import admin
from .models import Post, PostReader


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'title',)


@admin.register(PostReader)
class PostReaderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'reader', 'post',)
