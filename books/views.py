from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Book, Author
from .forms import ReviewForm

def books_list(request):
    books = Book.objects.order_by('title')
    return render(request, 'books/book_list.html', {'books': books})

def books_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'books/author_detail.html', {'author': author})

def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.published_date = timezone.now()
            review.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'books/add_review.html', {'form': form})
        
    
