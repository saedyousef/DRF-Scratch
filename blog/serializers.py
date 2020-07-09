from blog.models import Article, Category, Reaction
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.SerializerMethodField('likes_count')

    def likes_count(self, obj):
        return Reaction.objects.filter(article=obj).all().count()
    class Meta:
        model = Article
        fields = ['url', 'id', 'title', 'description', 'author', 'category', 'publish_date', 'likes']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'title', 'description']