from django.contrib import admin
from django.urls import path
#from .views import index_view
from .views import BookView, BookDetailView

app_name = 'library'

urlpatterns = [
    path('', BookView.as_view(), name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
