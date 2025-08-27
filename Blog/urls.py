from django.urls import path
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Detalhe pelo slug
]
