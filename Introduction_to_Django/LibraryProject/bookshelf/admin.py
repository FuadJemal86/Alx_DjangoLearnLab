from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these fields in the list view
    list_filter = ('publication_year', 'author')           # filters on the right
    search_fields = ('title', 'author')                    # search bar by title or author
