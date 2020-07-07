from django.contrib import admin
from blog.models import Category, Article
# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
