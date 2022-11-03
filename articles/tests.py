from django.test import TestCase
from .models import Article

class ArticleTestCase(TestCase):
    def test_create_article(self):
        article = Article.objects.create(title="This is the testing title", content="This is the testing content")
        print("article", article)
