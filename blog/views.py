from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import ArticleSerializer, UserSerializer, CategorySerializer
from blog.models import Article, Category
from django.contrib.auth.models import User
from rest_framework.views import APIView
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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['get']