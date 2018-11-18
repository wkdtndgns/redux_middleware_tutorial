from rest_framework import serializers
from .models import Type, Post, Image

class TypeSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Type
        fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Post
        fields = ('id', 'type', 'title', 'writer', 'context', 'created_at', 'updated_at')

class ImageSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Image
        fields = ('id', 'post', 'image_file')