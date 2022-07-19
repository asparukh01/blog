from django.urls import path

from .views.comment_views import CommentDeleteApiView, CommentCreateApiView
from .views.views import PostCreateApiView, PostUpdateApiView, PostDeleteApiView, PostPublicationView, PostRatingView

post_url = [
    path('post/create/', PostCreateApiView.as_view(), name='post_create_api'),
    path('post/update/<int:pk>/', PostUpdateApiView.as_view(), name='post_update_api'),
    path('post/delete/<int:pk>/', PostDeleteApiView.as_view(), name='post_delete_api'),
    path('post/<int:pk>/publication/', PostPublicationView.as_view(), name='post_publication'),
    path('post/<int:pk>/rating/', PostRatingView.as_view(), name='post_rating'),
]

comment_url = [
    path('post/<int:pk>/comment/create/', CommentCreateApiView.as_view(), name='comment_create_api'),
    path('post/comment/<int:pk>/delete/', CommentDeleteApiView.as_view(), name='comment_delete_api'),
]

urlpatterns = post_url
urlpatterns += comment_url
