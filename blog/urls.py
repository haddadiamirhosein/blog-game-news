from unicodedata import name
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('' , views.Home , name='home'),
    path('post/<slug:article_slug>' , views.detail_article , name="detail_article"),
    path('posts/' , views.posts , name="posts")
]