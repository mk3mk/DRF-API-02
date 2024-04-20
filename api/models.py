from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
  name = models.CharField(max_length=100)


class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  birth_year = models.IntegerField()
  # Для обратной связи с книгами
  # books = models.ManyToManyField('Book', related_name='authors_of_the_book')


class Book(models.Model):
  title = models.CharField(max_length=100)
  genre = models.ForeignKey(Genre,
                            on_delete=models.CASCADE,
                            related_name='books')
  authors = models.ManyToManyField('Author',
                                   related_name='books_of_the_author')


class Post(models.Model):
  title = models.CharField(max_length=100)
  text = models.TextField()
  image = models.ImageField(upload_to='posts/', blank=True, null=True)
  author = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='posts')
