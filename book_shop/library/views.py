from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, View


class BookView(ListView):
    # model = Book
    template_name = 'library/allbook.html'
    context_object_name = 'all_books'
    queryset = Book.objects.prefetch_related('author', 'review').all()


class BookDetailView(DetailView):
    queryset = Book.objects.prefetch_related('author', 'review').all()
    context_object_name = 'book'
    template_name = 'library/allbook_detail.html'
