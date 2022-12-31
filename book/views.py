from django.shortcuts import render
from .models import Category, Book
from django.shortcuts import get_object_or_404

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'book/home.html', context)

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug, in_stock=True)
    context = {
        'book': book,
    }
    return render(request, 'book/books/book_detail.html', context)

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'books': books,
    }
    return render(request, 'book/books/category.html', context)