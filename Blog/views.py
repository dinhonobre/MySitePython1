from django.shortcuts import render
from .models import Post  # Importa o modelo Post

def index(request):
    posts = Post.objects.all()  # Busca todos os posts no banco de dados
    return render(request, 'index.html', {'posts': posts})  # Passa para o template
