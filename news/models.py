from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from time import time


def gen_slug(slug: models.CharField) -> models.CharField:
    new_slug = slugify(slug, allow_unicode=True)
    new_slug += '-' + str(int(time()))
    return new_slug


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='news')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self) -> str:
        return reverse('news_content_url', kwargs={'slug': self.slug})

    def get_update_url(self) -> str:
        return reverse('news_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self) -> str:
        return reverse('news_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'News with title "{self.title}", slug "{self.slug}", ' \
               f'body "{self.body}" and date "{self.date}"'


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, unique=True)

    def get_absolute_url(self) -> str:
        return reverse('tag_content_url', kwargs={'slug': self.slug})

    def get_update_url(self) -> str:
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self) -> str:
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self) -> str:
        return f'Tag "{self.title}" with slug "{self.slug}"'
