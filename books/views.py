from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def books_list(request):
    books = Book.objects.order_by('title')
    return render(request, 'books/book_list.html', {'books': books})

def books_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'books/author_detail.html', {'author': author})
