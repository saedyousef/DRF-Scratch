from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import ArticleSerializer, CategorySerializer
from blog.models import Article, Category
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-publish_date')
    serializer_class = ArticleSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']