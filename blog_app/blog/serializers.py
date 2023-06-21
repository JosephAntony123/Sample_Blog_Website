from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'cover_photo', 'heading', 'subheadings', 'blog_text', 'created_datetime', 'author', 'conclusion')
        read_only_fields = ('created_date', 'author')

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user if request else None
        return BlogPost.objects.create(author=author, **validated_data)

    def update(self, instance, validated_data):
        instance.cover_photo = validated_data.get('cover_photo', instance.cover_photo)
        instance.heading = validated_data.get('heading', instance.heading)
        instance.subheadings = validated_data.get('subheadings', instance.subheadings)
        instance.blog_text = validated_data.get('blog_text', instance.blog_text)
        instance.conclusion = validated_data.get('conclusion', instance.conclusion)
        instance.save()
        return instance
