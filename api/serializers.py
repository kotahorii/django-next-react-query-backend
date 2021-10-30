from django.db.models import fields
from rest_framework import serializers
from .models import User, News, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True,
                                     'required': True, 'min_length': 5}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NewsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = News
        fields = ('id', 'content', 'created_at')


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)
    username = serializers.ReadOnlyField(
        source='user.username', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'username', 'user_id', 'created_at')
    extra_kwargs = {'user_id': {'read_only': True}}
