from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Book


def all_book(request):
    all_books = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('--update book error is %s' % e)
        return HttpResponse('The book is not existed')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        price = request.POST['price']
        book.price = price
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):

    book_id = request.GET.get('book_id')
    if not book_id:
        return HttpResponse('异常')

    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as err:
        print('delete book get error %s' % err)
        return HttpResponse('The book id is error')

    book.is_active = False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')

