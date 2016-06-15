from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    active = models.BooleanField(default=False)
    biography = models.TextField(default='biography not available')
    
    def __str__(self):
        return self.second_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, default=1)
    publication_date = models.DateField()
    description = models.TextField(default='OK')

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews")
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_review = models.BooleanField(default=False)

    def approve(self):
        self.approved_review = True
        self.save()
        
    def __str__(self):
        return self.text
        
    
class RateBook(models.Model):
    book = models.ForeignKey(Book, related_name="ratebook")
    rate_text = models.CharField(max_length=200, default="Love it!")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.rate_text

class RateAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.rate
