import pytest
from Blog.models import Post

@pytest.mark.django_db
def test_criacao_post():
    post = Post.objects.create(titulo="Meu Post", conteudo="Conteúdo de teste")
    assert post.titulo == "Meu Post"
