# bookshelf/views.py

from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # book creation logic
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # edit logic
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # delete logic
    pass



from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
