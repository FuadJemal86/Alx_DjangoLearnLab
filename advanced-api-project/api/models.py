from django.db import models

class Author(models.Model):
    """
    Represents an author who can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with a title, publication year, and an author.
    Each book is linked to one Author via a foreign key.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
