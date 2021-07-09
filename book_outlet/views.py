from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from .models import Book
# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    num_of_books=books.count()
    avg_rating=books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_of_books,
        "average_rating": avg_rating,
        })


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
