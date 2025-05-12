from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import UserSerializer

class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLogin(APIView):
    def post(self, request):
        print('request: ', request.data['username'], request.data['password'])
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print('user: ', user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'error':'Invalid Credentials'}, status=401)
        