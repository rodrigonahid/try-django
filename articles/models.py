from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.db.models import Q

from .utils import slugify_instance_title

class ArticleManager(models.Manager):
    def search(self, query):
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return Article.objects.filter(lookups)

class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects=ArticleManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/articles/{self.slug}/'

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)

pre_save.connect(article_pre_save, sender=Article)
post_save.connect(article_post_save, sender=Article)