from django.urls import path
from .views import post_view, home_view

urlpatterns = [
    path('', home_view, name='home'),  # rota raiz
    path('post/', post_view, name='post')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

