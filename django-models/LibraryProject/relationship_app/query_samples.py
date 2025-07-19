from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_orwell = author.books.all()
print("Books by George Orwell:", list(books_by_orwell))

# Query 2: List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", list(books_in_library))

# Query 3: Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of Central Library:", librarian.name)
