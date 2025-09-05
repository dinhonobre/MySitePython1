from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'created_at')
    ordering = ('created_at',)
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)
