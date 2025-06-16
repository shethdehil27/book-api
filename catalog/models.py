from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    category = models.CharField(max_length=100, blank=True)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=30)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
