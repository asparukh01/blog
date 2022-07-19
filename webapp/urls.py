from django.urls import path

from .views.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views.comment_views import CommentCreateView, CommentDeleteView, CommentListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post_detail/<int:pk>/comment/create', CommentCreateView.as_view(), name='comment_create'),
    path('post_detail/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post_detail/<int:pk>/comments/', CommentListView.as_view(), name='comment_list'),
]
