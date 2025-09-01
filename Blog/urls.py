from django.urls import path
from .views import index  # Só importa a view que realmente existe

urlpatterns = [
    path('', index, name='index'),  # Aponta a raiz para a view index
    # Se precisar, você pode criar outras rotas depois
]
