from django.shortcuts import render
from .models import Post

def home_view(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def post_view(request):
    return render(request, "post.html")
