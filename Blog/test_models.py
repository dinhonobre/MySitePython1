from django.test import TestCase
from django.contrib.auth.models import User
from Blog.models import Post, Comentario

class PostModelTest(TestCase):
    def setUp(self):
        # Criar usuário
        self.autor = User.objects.create_user(username="teste", password="12345")
        # Criar post com autor
        self.post = Post.objects.create(
            titulo="Título de Teste",
            conteudo="Conteúdo do post",
            autor=self.autor
        )

    def test_post_criado(self):
        self.assertEqual(self.post.titulo, "Título de Teste")

class ComentarioModelTest(TestCase):
    def setUp(self):
        # Criar usuário
        self.usuario = User.objects.create_user(username="teste2", password="12345")
        # Criar post com autor
        self.post = Post.objects.create(
            titulo="Post para Comentário",
            conteudo="Texto do post",
            autor=self.usuario
        )
        # Criar comentário
        self.comentario = Comentario.objects.create(
            post=self.post,
            autor=self.usuario.username,  # passar o nome como string
            texto="Comentário de teste"   # usar 'texto' e não 'conteudo'
        )

    def test_comentario_criado(self):
        self.assertEqual(self.comentario.texto, "Comentário de teste")  # usar 'texto'
