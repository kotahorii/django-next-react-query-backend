from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from . import serializers
from .models import Task, News


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
