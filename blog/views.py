from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from blog.serializers import ArticleSerializer, CategorySerializer
from blog.models import Article, Category
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed.
    """
    queryset = Article.objects.all().order_by('-publish_date')
    serializer_class = ArticleSerializer
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']


class ReactionViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def hello(self, request, **kwargs):
        return Response('Hello')