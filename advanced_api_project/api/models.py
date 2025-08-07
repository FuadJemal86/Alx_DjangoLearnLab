from django.db import models
from django.utils import timezone

# Author model: represents the author of one or more books
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's full name

    def __str__(self):
        return self.name


# Book model: represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Title of the book
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # ForeignKey creates a one-to-many relationship (one author, many books)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
