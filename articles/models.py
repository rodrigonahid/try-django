from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from .utils import slugify_instance_title
class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)

pre_save.connect(article_pre_save, sender=Article)
post_save.connect(article_post_save, sender=Article)