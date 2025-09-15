from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao')
    ordering = ('data_publicacao',)
    list_filter = ('status',)

admin.site.register(Post, PostAdmin)
