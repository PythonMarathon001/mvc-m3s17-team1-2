from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book


def book_list(request):
    context = {'book_list': Book.objects.all()}
    return render(request,'book/book_list.html',context)


def book_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request, 'book/book_form.html', {'form': form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/book/list')


def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/book/list')
