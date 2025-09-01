from django.test import TestCase
from Blog.models import Post, Comentario

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            titulo="Título de Teste",
            conteudo="Conteúdo do post"
        )

    def test_post_criado(self):
        self.assertEqual(self.post.titulo, "Título de Teste")
        self.assertEqual(self.post.conteudo, "Conteúdo do post")
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), "Título de Teste")


class ComentarioModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            titulo="Post para Comentário",
            conteudo="Texto do post"
        )
        self.comentario = Comentario.objects.create(
            post=self.post,
            autor="Anderson",
            texto="Comentário de teste"
        )

    def test_comentario_criado(self):
        self.assertEqual(self.comentario.autor, "Anderson")
        self.assertEqual(self.comentario.texto, "Comentário de teste")
        self.assertEqual(self.comentario.post, self.post)
        self.assertEqual(str(self.comentario), f"Anderson - {self.post.titulo}")
