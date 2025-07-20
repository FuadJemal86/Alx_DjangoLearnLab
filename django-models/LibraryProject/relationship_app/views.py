# relationship_app/views.py
from django.shortcuts import render
from .models import Book
# relationship_app/views.py
from django.views.generic.detail import DetailView
from .models import Library
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, '/relationship_app/list_books.html', {'books': books})


# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = '/relationship_app/library_detail.html'
    context_object_name = 'library'  # Name of the context variable to be passed to the template


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})