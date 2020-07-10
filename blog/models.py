from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publish_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name="cat")

    def __str__(self):
        return f"{self.title}"

    # Return likes count for each Article object.
    def likes_count(self):
        return Reaction.objects.filter(article=self).all().count()

# Reaction Model to store 'Likes' of an article.
class Reaction(models.Model):
    # Reaction type Constant
    LIKE = 'like'

    type = models.CharField(max_length=30)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name="reactions")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="likers")
    created  = models.DateField(auto_now=True)

