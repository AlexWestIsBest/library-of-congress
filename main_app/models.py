from django.db import models
from django.urls import reverse
# from colorfield.fields import ColorField

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=1000)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.id})

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
    # COLOR_PALETTE = [
    #     ("#FF5722", "deep-orange"),
    #     ("#4CAF50", "green"),
    #     ("#03A9F4", "light-blue"),
    #     ("#795548", "brown"),
    # ]

    title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    isbn = models.CharField(max_length=13)
    pageCount = models.PositiveIntegerField()
    pubDate = models.DateField('Publication Date')
    genre = models.CharField(max_length=2, choices=GENRES, default=GENRES[0][0])
    bookCover = models.CharField(max_length=1000)
    # bookColor = ColorField(samples=COLOR_PALETTE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.id})

