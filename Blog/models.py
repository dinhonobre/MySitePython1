from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Rascunho"),
    (1, "Publicado")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-data_publicacao"]

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=100, default="Desconhecido")
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.post.titulo}"
