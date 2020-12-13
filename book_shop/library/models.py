from django.db import models


class PublishingHouse(models.Model):
    name = models.CharField(max_length=32, unique=True)
    address = models.CharField(max_length=256)

    class Meta:
        unique_together = ['name', 'address']


class Author(models.Model):
    name = models.CharField(max_length=64)
    birthdate = models.DateField(null=True, blank=True)
    is_man = models.BooleanField(default=True)
    about = models.TextField(null=True)

    unique_together = ['name', 'birthdate']


class Review(models.Model):
    about_book = models.TextField(blank=True)
    author_review = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.about_book

    def review_count(self):
        return Review.objects.count()


class Book(models.Model):
    author = models.ManyToManyField(Author)
    release = models.DateField(null=False)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.PROTECT)
    isbn = models.IntegerField(unique=True)
    name_book = models.CharField(max_length=256, null=False)
    review = models.ManyToManyField(Review)
    image = models.ImageField(upload_to='book', blank=True, null=True)

    def __str__(self):
        return self.name_book
