from django.test import TestCase
from .models import Article
from .utils import slugify_instance_title
from django.utils.text import slugify

class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_articles = 250
        for i in range(0, self.number_of_articles):
            Article.objects.create(
                title="Hello World",
                content="That's the content"
            )
    def test_queryset_exists(self):
        articles = Article.objects.all()
        self.assertTrue(articles.exists())

    def test_queryset_count(self):
        articles = Article.objects.all()
        self.assertEqual(articles.count(), self.number_of_articles)

    def test_queryset_slug(self):
        articles = Article.objects.all().order_by("id").first()
        slugified_title = slugify(articles.title)
        self.assertEqual(articles.slug, slugified_title)

    def test_queryset_unique_slug(self):
        articles = Article.objects.exclude(slug__iexact='hello-world')
        for obj in articles:
            slugified_title = slugify(obj.title)
            self.assertNotEqual(obj.slug, slugified_title)

    def test_slugify_instance_title(self):
        articles = Article.objects.all().last()
        new_slugs = []

        for i in range(0, 25):
            instance = slugify_instance_title(articles)
            new_slugs.append(instance.slug)

        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))
        
    def test_query_search(self):
        articles = Article.objects.search(query="Hello world")
        self.assertEqual(len(articles), self.number_of_articles)
        articles = Article.objects.search(query="Hello")
        self.assertEqual(len(articles), self.number_of_articles)
        articles = Article.objects.search(query="That's the content")
        self.assertEqual(len(articles), self.number_of_articles)
