from rest_framework import serializers
from .models import Post, User, Book, Genre, Author


class PostSerializer(serializers.ModelSerializer):

  class Meta:
    model = Post
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  posts = PostSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = ['id', 'username', 'age', 'city', 'posts']


class BookSerializer(serializers.ModelSerializer):

  class Meta:
    model = Book
    fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

  class Meta:
    model = Genre
    fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):

  class Meta:
    model = Author
    fields = '__all__'
