from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"