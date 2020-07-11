import json
from rest_framework.test import force_authenticate
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from blog.models import Category, Article, Reaction
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

# Create your tests here.   
class APITestCase(APITestCase):

    def setUp(self):
        # Create users.
        admin = User.objects.create_superuser(username='superuser', password='SuperPWD', email='admin@admin.com')
        user = User.objects.create_user(username='testuser', password='TestPWD', email='testuser@testdomain.com')

        # Generate Authtoken for each user.
        token1 = Token.objects.create(user=user)
        token2 = Token.objects.create(user=admin)
        # Create Category.
        category1 = Category.objects.create(title='Category Title', description='Category Description')
        category2 = Category.objects.create(title='Category Titl2', description='Category Description2')

        # Create Articles.
        article1 = Article.objects.create(title='Article 1', description='Description 1', author=admin, category=category1)
        article2 = Article.objects.create(title='Article 2', description='Description 2', author=admin, category=category1)
        article3 = Article.objects.create(title='Article 3', description='Description 3', author=admin, category=category2)

    # Testing categories count.
    def test_categories_count(self):
        categories = Category.objects.all()
        self.assertEqual(categories.count(), 2)

    # Testing Articles count.
    def test_categorized_articles(self):
        category = Category.objects.get(pk=1)
        articles = Article.objects.filter(category=category).all()
        self.assertEqual(articles.count(), 2)


    def test_reaction(self):
        token = Token.objects.get(user__username='testuser')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        data = {
            'article_id': 1
        }
        url = reverse('react-react')

        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_article_list(self):
        client = APIClient()
        url = reverse('article-list')
        data = {}
        response = client.get(url, data, format=json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_article_list_count(self):
        client = APIClient()
        url = reverse('article-list')
        data = {}
        response = client.get(url, data, format=json)
        count = json.loads(response.content)
        self.assertEqual(count['count'], 3)
    

    def test_category_list_count(self):
        client = APIClient()
        url = reverse('category-list')
        data = {}
        response = client.get(url, data, format=json)
        count = json.loads(response.content)
        self.assertEqual(count['count'], 2)