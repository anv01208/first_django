from django.urls import path
from .views import *

urlpatterns = [
    path('books', BooksView, name='books_url'),
    path('book/<int:book_id>', BookView,name='book_url'),
    path('create_book',BookCreateView,name='book_create_url'),
    path('update_book/<int:book_id>',BookUpdateView,name='book_update_url'),

]
