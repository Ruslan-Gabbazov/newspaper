from django.db import models
from django.urls import reverse


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='news')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self) -> str:
        return reverse('news_content_url', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'News with title 'f'{self.title}'', slug 'f'{self.slug}'', ' \
               'body 'f'{self.body}'' and date 'f'{self.date}'''


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, unique=True)

    def get_absolute_url(self) -> str:
        return reverse('tag_content_url', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'Tag 'f'{self.title}'' with slug 'f'{self.slug}'''
