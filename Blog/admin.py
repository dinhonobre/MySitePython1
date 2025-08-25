from django.contrib import admin
from .models import Post  # importe o model Post

admin.site.register(Post)  # registre o model no Admin
