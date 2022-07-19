from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Comment
from ..serializer import CommentSerializer
from webapp.models import Post


class CommentCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        pk = str(request).split('/')
        id = int(pk[3])
        if serializer.is_valid():
            serializer.save(author=request.user, post=Post.objects.get(id=id))
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class CommentDeleteApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        objects = get_object_or_404(Comment, pk=kwargs.get('pk'))
        objects.delete()
        return Response({"status": "success", "data": objects.pk})
