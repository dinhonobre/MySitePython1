from django.urls import path
from . import views

app_name = "Blog"  # necessário para usar {% url 'Blog:post_list' %}

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]
