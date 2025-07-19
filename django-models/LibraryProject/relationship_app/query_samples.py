from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        # Use filter to get all books by the specific author
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using filter here
        if books.exists():
            for book in books:
                print(book.title)
        else:
            print(f"No books found for author {author_name}.")
    except Author.DoesNotExist:
        print("Author not found.")
