from django.test import TestCase
from .models import Review, Author
from django.test import Client
from django.urls import reverse
from .views import BookView

class TestModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='Фёдор Иванович Тютчев',
            about='русский лирик, поэт-мыслитель, дипломат'
        )
        self.review = Review.objects.create(about_book='Хорошие стихи', author_review=self.author, rating=5)

    def tearDown(self):
        Author.objects.all().delete()
        Review.objects.all().delete()

    def test_review_str(self):
        self.assertEqual('Хорошие стихи', str(self.review))

    def test_review_count_before_add(self):
        Author.objects.all().delete()
        Review.objects.all().delete()
        self.assertEqual(self.review.review_count(), 0)

    def test_review_count_after_add(self):
        self.assertEqual(self.review.review_count(), 1)


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        pass

    def test_index(self):
        url = reverse('library:index')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_context_paginate(self):
        response = self.client.get('/')
        self.assertEqual(response.context['is_paginated'], False)

    def test_page_not_found(self):
        response = self.client.get('/test')
        self.assertEqual(404, response.status_code)
