from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"
    
    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name="cat")

    def __str__(self):
        return f"{self.title}"