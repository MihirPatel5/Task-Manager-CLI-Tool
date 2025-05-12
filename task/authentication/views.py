from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializer import UserSerializer, TaskSerializer
from .models import Task, IsAdminOrManager
from rest_framework.permissions import IsAuthenticated

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
        

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = user.profile.role
        if role == 'employee':
            return Task.objects.filter(assigned_to=user)
        return Task.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminOrManager()]
        return [IsAuthenticated()]
