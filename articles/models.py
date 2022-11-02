from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(auto_now=True)
    publish = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title