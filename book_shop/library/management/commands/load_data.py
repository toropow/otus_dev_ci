from django.core.management.base import BaseCommand, CommandError
from library.models import Author, PublishingHouse, Review, Book


class Command(BaseCommand):
    help = 'my command'

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Review.objects.all().delete()
        Book.objects.all().delete()
        PublishingHouse.objects.all().delete()

        ph_first = PublishingHouse.objects.create(name='Издательство 1', address='Москва')
        ph_second = PublishingHouse.objects.create(name='Издательство 2', address='Санкт-Петербург')
        PublishingHouse.objects.create(name='Издательство 3', address='Нижний новогород')

        esenin = Author.objects.create(name='Сергей Александрович Есенин', birthdate='1895-10-03', is_man=True,
                                       about='Великий классик')
        pushkin = Author.objects.create(name='Александ Сергеевич Пушкин', birthdate='1799-06-06', is_man=True,
                                        about='Великий поэт')
        ahmatova = Author.objects.create(name='Анна Андреевна Ахматова', birthdate='1889-06-23', is_man=False,
                                         about='Великая поэтесса')
        user_review = Author.objects.create(name='Иванов Иван Иванович', birthdate='2000-11-11', is_man=True,
                                            about='Литературный критик')
        review_first = Review.objects.create(about_book='Супер книга', author_review=user_review, rating=10)
        review_second = Review.objects.create(about_book='Топчик', author_review=user_review, rating=10)
        pugachev = Book.objects.create(release='1924-10-03', publishing_house=ph_first, isbn=123,
                                       name_book='Пугачев')
        pugachev.author.add(esenin)
        pugachev.author.add(ahmatova)
        pugachev.review.add(review_first)

        evg_onegin = Book.objects.create(release='1954-11-20', publishing_house=ph_second, isbn=456,
                                          name_book='Евгений Онегин')
        evg_onegin.author.add(pushkin)
        evg_onegin.review.add(review_first)
        evg_onegin.review.add(review_second)
