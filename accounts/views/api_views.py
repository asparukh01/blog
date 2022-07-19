import json

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import CustomUser
from ..serializer import CustomUserSerializer, KarmaSerializer


class LogoutViewApi(APIView):

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class ProfileUpdateView(APIView):
    def get(self, request, *args, **kwargs):
        objects = get_object_or_404(CustomUser, pk=kwargs.get('pk'))
        serializer = CustomUserSerializer(objects)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        objects = get_object_or_404(CustomUser, pk=kwargs.get('pk'))
        serializer = CustomUserSerializer(objects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ProfileKarmaView(APIView):

        def patch(self, request, *args, **kwargs):
            account = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
            data = json.loads(self.request.body)
            serializer = KarmaSerializer(account, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
