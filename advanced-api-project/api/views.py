from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

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
