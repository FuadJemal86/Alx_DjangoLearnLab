# relationship_app/views.py
from django.shortcuts import render
from .models import Book
# relationship_app/views.py
from django.views.generic import DetailView
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, '/list_books.html', {'books': books})


# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = '/library_detail.html'
    context_object_name = 'library'  # Name of the context variable to be passed to the template
