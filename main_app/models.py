from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField

# Create your models here.
class Book(models.Model):
    GENRES = (
        ('MY', 'Mystery'),
        ('TH', 'Thriller'),
        ('CO', 'Coming of Age'),
        ('HI', 'Historical Fiction'),
        ('FA', 'Fantasy'),
        ('MA', 'Magical Realism'),
        ('LF', 'Literary Fiction'),
        ('RE', 'Realistic Fiction'),
        ('SC', 'Science Fiction'),
        ('RO', 'Romance'),
        ('HO', 'Horror'),
        ('WE', 'Western'),
        ('DY', 'Dystopian'),
    )
    COLOR_PALETTE = [
        ("#FF5722", "deep-orange"),
        ("#4CAF50", "green"),
        ("#03A9F4", "light-blue"),
        ("#795548", "brown"),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    pageCount = models.PositiveIntegerField()
    pubDate = models.DateField('Publication Date')
    genre = models.CharField(max_length=2, choices=GENRES)
    bookCover = models.CharField(max_length=1000)
    bookColor = ColorField(samples=COLOR_PALETTE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.id})

