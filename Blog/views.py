from django.shortcuts import render, get_object_or_404
from .models import Post

# Página inicial: mostra apenas posts publicados
def index(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'index.html', {'posts': posts})

# Página de detalhe do post usando slug
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
