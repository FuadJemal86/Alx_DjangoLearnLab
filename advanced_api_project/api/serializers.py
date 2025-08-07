from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer: Serializes Book model and includes validation for publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer: Serializes Author model including nested books using BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization of related books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
