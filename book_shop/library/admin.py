from django.contrib import admin
from .models import Book, PublishingHouse, Review, Author


admin.site.register(Book)
admin.site.register(PublishingHouse)
admin.site.register(Review)
admin.site.register(Author)