from django.db import models

# Create your models here.
class Author(models.Model):  
    full_name = models.TextField(verbose_name='Автор')  
    birth_year = models.SmallIntegerField(verbose_name='Год рождения')  
    country = models.CharField(max_length=2, verbose_name='Страна')

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'автор'
        ordering = [ 'full_name' ]

    def __str__(self):
        return self.full_name


class Book(models.Model):  
    ISBN = models.CharField(max_length=13, verbose_name='Междунар. код')  
    title = models.TextField(verbose_name='Наименование')  
    description = models.TextField(verbose_name='Аннотация')  
    year_release = models.SmallIntegerField(verbose_name='Издание')  
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор', related_name='entries')
    copy_count = models.SmallIntegerField(default=1, verbose_name='Экз')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT, null=True, verbose_name='Издательство', related_name='entries')

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'книга'
        ordering = [ 'publisher' ]

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=20,verbose_name='Издательство')
    country = models.CharField(max_length=2, verbose_name='Страна')

    class Meta:
        verbose_name_plural = 'Издательства'
        verbose_name = 'издательство'
        ordering = [ 'title' ]

    def __str__(self):
        return self.title


    
      