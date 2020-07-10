import json
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
    def test_articles_count(self):
        articles = Article.objects.all()
        self.assertEqual(articles.count(), 3)


    def test_obtain_token(self):
        url = reverse('get_auth_toekn')
        data = {
            'username': 'testuser',
            'password': 'TestPWD'
        }

        response = self.client.post(url, data, format='json')
        token = json.loads(response.content)['token']
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reaction(self):
        user = User.objects.get(username='testuser')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('react-react')
        data = {
            'article_id': 1
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
