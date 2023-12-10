from django.http import HttpResponse, HttpRequest, JsonResponse, Http404
from datetime import datetime
from random import choice, randint

books = [
    {"id": 1, "title": "Book1", "author": "Author1"},
    {"id": 2, "title": "Book2", "author": "Author2"},
]

def get_object_or_404(all_books: list, id_: int) -> dict:
    for book in all_books:
        if book["id"] == id_:
            return book
    raise Http404


def index(request: HttpRequest) -> HttpResponse:
    #request.method == "GET"
    #return HttpResponse(f"<h1>Добро пожаловать в библиотеку!!!</h1> Запрос был выполнен методом {request.method}")
    return HttpResponse(f"<h1>Добро пожаловать в библиотеку!!!</h1>")


def about_handler(request):
    now = datetime.now()
    return HttpResponse(f"Сайт разработан в {now.year}.")


def books_list(request):
    return JsonResponse(books, safe=False, json_dumps_params={"ensure_ascii": False, "indent": 4})


def random_book(request):
    book = choice(books)
    return JsonResponse(book, json_dumps_params={"ensure_ascii": False, "indent": 4})


def random_book_with_missing(request):
    id_ = randint(0, 10)
    book = get_object_or_404(books, id_)
    return JsonResponse(book, json_dumps_params={"ensure_ascii": False, "indent": 4})

