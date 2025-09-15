from django.shortcuts import render, get_object_or_404
from .models import Post

# Página inicial, lista apenas posts publicados
def post_list(request):
    posts = Post.objects.filter(status=1)  # 1 = publicado
    return render(request, 'Blog/index.html', {'posts': posts})

# Detalhe de um post por slug
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, 'Blog/post_detail.html', {'post': post})

# Home pode ser um alias para post_list
def home_view(request):
    return post_list(request)
