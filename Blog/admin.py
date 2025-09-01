from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'status')  # mostra título, data e status
    list_filter = ('status', 'data_publicacao')             # filtros no Admin
    search_fields = ('titulo', 'conteudo')                 # busca rápida
    ordering = ('-data_publicacao',)                       # ordena do mais recente

admin.site.register(Post, PostAdmin)
