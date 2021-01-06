from django.contrib import admin
from .models import Book, Author, Publisher

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ('ISBN', 'title', 'description',  'author', 'year_release', 'publisher', 'price', 'copy_count')
    list_display = ('ISBN', 'title', 'description', 'author', 'year_release', 'publisher', 'copy_count', 'price')
    list_display_links = ('title', 'author', 'publisher')
    search_fields = ('title', 'description')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country')
    list_display_links = ('full_name', 'birth_year')
    search_fields = ('full_name', 'birth_year', 'country')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'country')
    list_display_links = ('title', 'country')
    search_fields = ('title', 'country')





    
