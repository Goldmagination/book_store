from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {"books": books})


def book_detail(request, slug):
    # try:
    #     defined_book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    defined_book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": defined_book.title,
        "author": defined_book.author,
        "rating": defined_book.rating,
        "is_bestselling": defined_book.is_bestselling,
        "price": defined_book.price,
    })
