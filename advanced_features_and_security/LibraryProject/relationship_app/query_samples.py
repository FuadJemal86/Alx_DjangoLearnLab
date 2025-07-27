from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author using filter
def books_by_author(author_name):
    try:
        # Use filter to get all books by the specific author
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using filter to query books
        if books.exists():
            for book in books:
                print(book.title)
        else:
            print(f"No books found for author {author_name}.")
    except Author.DoesNotExist:
        print("Author not found.")

# List all books in a library using filter
def books_in_library(library_name):
    try:
        # Get library using name and then filter books
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Directly use the related name to get books
        if books.exists():
            for book in books:
                print(book.title)
        else:
            print(f"No books found in {library_name}.")
    except Library.DoesNotExist:
        print("Library not found.")

# Retrieve the librarian for a library using Librarian.objects.get()
def librarian_of_library(library_name):
    try:
        # Get the librarian for the specified library using Librarian.objects.get()
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Using Librarian.objects.get()
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("Librarian not found for this library.")
