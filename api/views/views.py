import json

from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Post
from ..serializer import PostSerializer, PostPublicationSerializer, PostRatingSerializer


class PostCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class PostUpdateApiView(APIView):
    def patch(self, request, *args, **kwargs):
        objects = get_object_or_404(Post, pk=kwargs.get('pk'))
        serializer = PostSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class PostDeleteApiView(APIView):
    def delete(self, request, *args, **kwargs):
        objects = get_object_or_404(Post, pk=kwargs.get('pk'))
        objects.delete()
        return Response({"status": "success", "data": objects.pk})


class PostPublicationView(APIView):

    def patch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        data = json.loads(self.request.body)
        serializer = PostPublicationSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostRatingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        data = json.loads(self.request.body)
        serializer = PostRatingSerializer(post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
