from django.core.management.base import BaseCommand
from p_library.models import Book, Author, Publisher
from collections import Counter
from django.db.models import Count

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

publishers = Publisher.objects.all()
books = Book.objects.all()
authors = Author.objects.all()

# q = Publisher.objects.annotate(cnt=Count('entries'))


# for i in q:
#     print(i.title, i.cnt)

# for pub in publishers:
#     print(f'Издательство: {pub.title} | Страна: {pub.country} | книга: {pub.entries}')

# for book in books:
#     print(f'Название: {book.title} | Автор: {book.author} | Издательство: {book.publisher}')

# for aut in authors:
#     print(f'Автор: {aut.full_name} | Книга: {aut.entries}')

for pub in publishers:
    print(pub.title)
    for book in books:
        # print(pub.title, type(pub.title), book.publisher.title, type(book.publisher.title), book.title)
        if book.publisher.title == pub.title:
            print(f'\t{book.title}')