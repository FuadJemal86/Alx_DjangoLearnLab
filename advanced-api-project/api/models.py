from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_posted']  # Latest posts first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Redirect to detail page after create/update
        return reverse('post-detail', kwargs={'pk': self.pk})