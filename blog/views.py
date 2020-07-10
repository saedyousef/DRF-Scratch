from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from blog.serializers import ArticleSerializer, CategorySerializer, ReactionSerializer
from blog.models import Article, Category, Reaction
from blog.validations import Validations
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
    """
    API endpoint that allows register users to react(Like) an article.

    """

    # Mapping serlaizer class.
    serializer_class = ReactionSerializer

    # Authentications is required to make this action.
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def react(self, request, **kwargs):
        if request.data.get('article_id') is None or request.data.get('article_id') == "":
            return Response({'detail':'article_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        article_id = request.data.get('article_id')

        # Create new instance.
        validation = Validations()

        # Checks if the article is exist.
        article = validation.check_article(article_id)
        if not article:
            return Response({'detail':'No article found with this id'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the user is already reacted to this article.
        if not validation.is_valid_reaction(article, request.user):
            return Response({'detail':'You cannot react to this article more than once!'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Store the reaction.
        Reaction.objects.create(article=article, user=request.user, type=Reaction.LIKE)

        # Return response.
        return Response({'detail':'Your reaction have been stored successfully!'}, status=status.HTTP_201_CREATED)


