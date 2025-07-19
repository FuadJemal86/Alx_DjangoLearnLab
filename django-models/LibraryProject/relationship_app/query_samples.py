from relationship_app.models import Author, Book, Library

# 1. Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = author.books.all()
print("Books by George Orwell:", list(books_by_author))
# Expected Output: Books by George Orwell: [<Book: 1984>, <Book: Animal Farm>]

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", list(books_in_library))
# Expected Output: Books in Central Library: [<Book: 1984>, <Book: Brave New World>]

# 3. Retrieve the librarian for a library
librarian = library.librarian
print("Librarian of Central Library:", librarian.name)
# Expected Output: Librarian of Central Library: Fuad Jemal
