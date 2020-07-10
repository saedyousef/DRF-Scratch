from blog.models import Article, Category, Reaction
from rest_framework import serializers


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    likes = serializers.SerializerMethodField('count')

    def count(self, obj):
        return obj.likes_count()
    class Meta:
        model = Article
        fields = ['url', 'id', 'title', 'description', 'author', 'category', 'publish_date', 'likes']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'title', 'description']

class ReactionSerializer(serializers.Serializer):
    article_id = serializers.IntegerField(required=True, allow_null=False)