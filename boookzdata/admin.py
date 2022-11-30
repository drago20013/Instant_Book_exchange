from django.contrib import admin
from .models import Book, Category, Author, BookCondition, BookSite, Comment, Image, BookGiveawayShelf, BookShelf, \
    BookWantedShelf
from django.contrib.auth.models import Group

# Register your models here.


admin.site.register(Image)
admin.site.register(Book)
admin.site.register(BookShelf)
admin.site.register(BookWantedShelf)
admin.site.register(BookGiveawayShelf)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(BookCondition)
admin.site.register(BookSite)
admin.site.register(Comment)

admin.site.unregister(Group)

admin.site.site_header = 'Boookz Admin Panel'

