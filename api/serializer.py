from rest_framework import serializers

# from webapp.models import Post, Comment
from webapp.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'link', 'text', 'category', 'status']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_text']


class PostPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['publicated_at', 'status']


class PostRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['rating']
