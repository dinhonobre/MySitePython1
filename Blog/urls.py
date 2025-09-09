from django.urls import path
from .views import home_view, post_view

urlpatterns = [
    path('', home_view, name='home'),
    path('post/', post_view, name='post'),
]
