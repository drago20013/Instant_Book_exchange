from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField
from polymorphic.models import PolymorphicModel


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    url = models.TextField()

    def __str__(self):
        return self.name


class BookCondition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ManyToManyField('boookzdata.Image', related_name='books')

    book_shelf = models.ForeignKey('boookzdata.BookShelf', on_delete=models.CASCADE, related_name='books',
                                   related_query_name='book')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class BookShelf(PolymorphicModel):
    book_reader = models.ForeignKey('authentication.BookReader', on_delete=models.CASCADE, related_name='book_shelfs',
                                    related_query_name='book_shelfs')


class GiveawayBookshelf(BookShelf):
    pass

    def __str__(self):
        return f"{self.book_reader.user}'s give-away shelf"


class WantedBookshelf(BookShelf):
    pass

    def __str__(self):
        return f"{self.book_reader.user}'s wanted shelf"


class BookSite(models.Model):
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='sites', related_query_name='site')
    book_condition = models.ForeignKey(BookCondition, on_delete=models.CASCADE, related_name='sites',
                                       related_query_name='site')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    url = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class CustomerReportRecord(models.Model):
    time_raised = models.DateTimeField(default=timezone.now, editable=False)
    reference = models.CharField(unique=True, max_length=20)
    description = models.TextField()