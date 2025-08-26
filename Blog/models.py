from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicada'),
    )

    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  # ✅ Campo status
    slug = models.SlugField(unique=True, blank=True)  # ✅ Campo slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)  # ✅ Gera slug automaticamente pelo título
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.post.titulo}"
