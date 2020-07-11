from django.contrib.auth.models import User
from blog.models import Article, Reaction

class Validations():
    # Check if the user has already reacted(liked) to this article.
    def is_valid_reaction(self, article, user):
        reaction = Reaction.objects.filter(article=article, user=user)

        if reaction.count() != 0:
            return False
        else:
            return True

    # Check if article is exists.
    def check_article(self, article_id):
        if not isinstance(article_id, int):
            if not article_id.isnumeric():
                return False
            else:
                article_id = int(article_id)
        
        if not Article.objects.filter(pk=article_id).exists():
            return False
        else:
            return Article.objects.get(pk=article_id)

        
        