from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import BlogAuthor


class BlogAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogAuthor
        fields = ('name', 'bio', 'prof_img')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogAuthor
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = BlogAuthor.objects.create_user(
            validated_data['email'], validated_data['name'], validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
