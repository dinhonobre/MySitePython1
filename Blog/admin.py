from django.contrib import admin
from .models import Post, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'data_publicacao')
    list_filter = ('status',)
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'post', 'data_comentario')
