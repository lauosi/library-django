from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey('News', related_name="comments")
    author = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    

