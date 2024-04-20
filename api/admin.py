from django.contrib import admin
from .models import Post
from .models import Genre
from .models import Author
from .models import Book

admin.site.register(Post)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
