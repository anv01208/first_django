from django.shortcuts import render,redirect
from .models import *
from django import forms

from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
def BooksView(request):
    genre_name = request.GET.get('genre')

    if genre_name is not None:
        genre_name = genre_name.lower()

        try:
            genre = Genre.objects.get(type=genre_name)
            all_books = Book.objects.filter(genre=genre)
        except Genre.DoesNotExist:
            all_books = []
    else:
        all_books = Book.objects.all()

    context = {
        'books': all_books,
        'message': 'Welcome to BookShelves'
    }
    return render(request=request, template_name='books_template.html', context=context)

def BookView(request,book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request=request, template_name='book_template.html',context=context)

def BookCreateView(request):
    if request.method == 'GET':
        book_writer = Writer.objects.all()
        book_genre = Genre.objects.all()
        context = {
            'book_writer' : book_writer,
            'book_genre' : book_genre
        }
        return render(request=request,template_name='book_create_template.html',context=context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        book_writer = Writer.objects.get(id=request.POST.get('book_writer'))
        book_genre = Genre.objects.get(id=request.POST.get('book_genre'))
        rating = request.POST.get('rating')
        image = request.FILES.get('image')
        book = Book(title=name,description=description,release_date=release_date,image=image,genre=book_genre,author=book_writer,rating=rating)
        book.save()
        return redirect(BooksView)

def BookUpdateView(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method =='GET':
        book_genre = Genre.objects.all()
        book_writer = Writer.objects.all()
        context  ={
            'book' : book,
            'book_genre' : book_genre,
            'book_writer':book_writer
        }
        return render(request=request,template_name='book_update_template.html',context=context)
    elif request.method == 'POST':
        book.title = request.POST.get('name')
        book.description = request.POST.get('description')
        book.release_date = request.POST.get('release_date')
        book.rating = request.POST.get('rating')
        if request.POST.get('book_writer'):
            book.author= Writer.objects.get(id=request.POST.get('book_writer'))
        if request.POST.get('book_genre'):
            book.genre = Genre.objects.get(id=request.POST.get('book_genre'))

        if 'image' in request.FILES:
            book.image = request.FILES.get('image')
        book.save()
        return redirect('books_url')
