from django.urls import path

from posts.views_cbv import (PostListView, PostDetailView, CreatePostView,
                             PostUpdateView, PostDeleteView)
from . import views

app_name = 'posts'

urlpatterns = [
    # CRUD посты FBV
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),

    # CRUD посты CBV
    path('cbv/', PostListView.as_view(), name='index'),
    path('cbv/posts/<int:post_id>/', PostDetailView.as_view(),
         name='post_detail'),
    path('cbv/create/', CreatePostView.as_view(), name='post_create'),
    path('cbv/posts/<int:post_id>/edit/', PostUpdateView.as_view(),
         name='post_edit'),
    path('cbv/posts/<int:post_id>/delete/', PostDeleteView.as_view(),
         name='post_delete'),
]
