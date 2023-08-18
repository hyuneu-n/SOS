from rest_framework import serializers

from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("pk", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    published_date = serializers.DateTimeField(format="%D %H:%M", read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "title", "body", "image", "published_date", "comments")

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "body", "image")