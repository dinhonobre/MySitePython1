from django.shortcuts import render, get_object_or_404
from .models import Post

# Lista todos os posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# Detalhe de um post por slug
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})
