from rest_framework import generics, permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books.
    Open to any user (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<pk>/
    Returns detail of a single book by ID.
    Open to any user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Example of custom behavior on create:
        # Here you could add extra logic, like logging or setting owner.
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<pk>/update/
    Updates an existing book.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Additional custom update logic if needed
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<pk>/delete/
    Deletes a book by ID.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering support.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Add filter backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Enable filtering on fields
    filterset_fields = ['title', 'author__name', 'publication_year']  

    # Enable search on fields (text search)
    search_fields = ['title', 'author__name']

    # Enable ordering on fields
    ordering_fields = ['title', 'publication_year']

    # Optional: default ordering
    ordering = ['title']